"""'Entry / What it does' tables -> one sub-heading per row (rules: every operator/setting its own sub-heading).
Tables inside Adjust Last Operation sections stay (rules allow a property table there).
Under an h6 there is no deeper heading, so those rows become a list: - **Name**: description."""
import re, sys, pathlib
ALO = re.compile(r"^(repeat last|last operator|adjust last operation)", re.I)
HDR = re.compile(r"^\|\s*(Entry|Option|Item)\s*\|\s*What it does\s*\|", re.I)
def cells(row):
    row = row.strip()
    if row.startswith("|"): row = row[1:]
    if row.endswith("|"): row = row[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", row)]
def paras(t):
    t = re.sub(r"\s*<br\s*/?>\s*", "\n\n", t).strip()
    return t
def convert(text):
    lines = text.split("\n"); out = []; L = 0; inalo = False; fence = False; n = {"tables": 0, "rows": 0, "lists": 0}
    i = 0
    while i < len(lines):
        l = lines[i]
        if l.startswith("```"): fence = not fence
        m = None if fence else re.match(r"^(#{1,6})\s+(.*)", l)
        if m: L = len(m.group(1)); inalo = bool(ALO.match(m.group(2)))
        if not fence and HDR.match(l) and not inalo and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i+1]):
            j = i + 2; rows = []
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                rows.append(cells(lines[j])); j += 1
            n["tables"] += 1
            while out and out[-1].strip() == "": out.pop()
            out.append("")
            if L >= 6:
                n["lists"] += 1
                for c in rows:
                    name, desc = c[0], " ".join(c[1:]).strip()
                    desc = re.sub(r"\s*<br\s*/?>\s*", " ", desc)
                    out.append(f"- **{name}**: {desc}" if name and desc else (f"- **{name}**" if name else f"- {desc}"))
                    n["rows"] += 1
                out.append("")
            else:
                lv = max(L, 1) + 1 if L else 2
                for c in rows:
                    name, desc = c[0], paras(" | ".join(c[1:]))
                    if name:
                        out += ["#" * lv + " " + name, ""]
                    if desc: out += [desc, ""]
                    n["rows"] += 1
            while j < len(lines) and lines[j].strip() == "": j += 1
            i = j; continue
        out.append(l); i += 1
    return "\n".join(out), n
if __name__ == "__main__":
    tot = {"tables": 0, "rows": 0, "lists": 0}
    for p in sys.argv[1:]:
        t = pathlib.Path(p).read_text(); new, s = convert(t)
        if new != t: pathlib.Path(p).write_text(new)
        for k in tot: tot[k] += s[k]
    print(tot)
