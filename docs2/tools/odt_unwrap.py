#!/usr/bin/env python3
"""Pre-process a Bforartists manual .odt so Pandoc keeps its structure.

What it fixes (found in the Spike 1 inventory):
  * Title table   : 2-cell table [icon | "17 Editors - Timeline"] -> a Heading 1 paragraph
                    with the icon image in front (the converter reads the icon from it).
  * Banner tables : 1-cell tables that only wrap headings/paragraphs -> their contents.
                    Pandoc drops headings that sit inside a table cell.
Real data tables (more than one column, or no headings) are left alone.

Usage: odt_unwrap.py in.odt out.odt
"""
import sys, zipfile, shutil
from lxml import etree

NS = {
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "draw": "urn:oasis:names:tc:opendocument:xmlns:drawing:1.0",
}
T = "{%s}" % NS["table"]
X = "{%s}" % NS["text"]


def cells(tbl):
    return tbl.findall(".//table:table-cell", NS)


def unwrap(tbl, children):
    parent = tbl.getparent()
    idx = parent.index(tbl)
    for i, c in enumerate(children):
        parent.insert(idx + i, c)
    parent.remove(tbl)


def process(xml_bytes):
    root = etree.fromstring(xml_bytes)
    stats = {"title": 0, "banner": 0, "kept": 0}
    body = root.find(".//{urn:oasis:names:tc:opendocument:xmlns:office:1.0}text")
    first_table_seen = False
    for tbl in list(root.iter(T + "table")):
        if tbl.getparent() is None:
            continue
        cs = cells(tbl)
        cols = tbl.findall("table:table-column", NS)
        ncols = sum(int(c.get(T + "number-columns-repeated", "1")) for c in cols)
        rows = tbl.findall(".//table:table-row", NS)
        # Title table: first table in the document, 1 row, 2 cells, an image + a numbered title
        if not first_table_seen and len(rows) == 1 and len(cs) == 2:
            text = "".join(cs[1].itertext()).strip()
            if text and cs[0].find(".//draw:image", NS) is not None:
                h = etree.Element(X + "h")
                h.set(X + "outline-level", "1")
                frame = cs[0].find(".//draw:frame", NS)
                h.append(frame)
                frame.tail = text
                unwrap(tbl, [h])
                stats["title"] += 1
                first_table_seen = True
                continue
        first_table_seen = True
        # Banner table: a single cell
        if ncols == 1 and len(cs) == 1:
            unwrap(tbl, list(cs[0]))
            stats["banner"] += 1
            continue
        stats["kept"] += 1
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8"), stats


def main(src, dst):
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(dst, "w") as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "content.xml":
                data, stats = process(data)
            # mimetype must stay first and stored
            ct = zipfile.ZIP_STORED if item.filename == "mimetype" else zipfile.ZIP_DEFLATED
            zout.writestr(item, data, compress_type=ct)
    print(f"{src}: {stats}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
