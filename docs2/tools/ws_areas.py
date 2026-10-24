#!/usr/bin/env python3
"""Find the editor areas in a workspace screenshot (Docs 2.0, workspace maps).

    python3 docs2/tools/ws_areas.py <screenshot.png> [--overlay out.png]

Bforartists draws a 3 px near-black gap (#161616) between areas. The window is split like a
guillotine: find a gap that crosses the whole rectangle, split, repeat. Prints one box per area
as percentages of the image (left, top, width, height), the format the workspace maps use.
Screenshots taken with ws_capture.py carry exact boxes from Bforartists itself instead.
"""
import json
import sys

import numpy as np
from PIL import Image, ImageDraw

GAP = (14, 30)          # grey value range of the gap colour
MIN_AREA = 40           # px: smaller pieces are not areas


def gap_mask(img):
    a = np.asarray(img.convert("RGB")).astype(int)
    lo, hi = GAP
    m = (a[..., 0] >= lo) & (a[..., 0] <= hi) & (abs(a[..., 0] - a[..., 1]) < 3) & (abs(a[..., 1] - a[..., 2]) < 3)
    return m


def content_box(img):
    """Skip a light window title bar (Windows / macOS chrome) and borders."""
    a = np.asarray(img.convert("L")).astype(int)
    h, w = a.shape
    top = 0
    while top < h // 5 and a[top, w // 4: 3 * w // 4].mean() > 150:
        top += 1
    return [0, top, w, h]


def runs(flags):
    out, s = [], None
    for i, f in enumerate(flags):
        if f and s is None:
            s = i
        if not f and s is not None:
            out.append((s, i))
            s = None
    if s is not None:
        out.append((s, len(flags)))
    return out


def split(m, box, depth=0):
    x0, y0, x1, y1 = box
    if depth > 12 or x1 - x0 < MIN_AREA * 2 and y1 - y0 < MIN_AREA * 2:
        return [box]
    sub = m[y0:y1, x0:x1]
    for axis in (1, 0):        # vertical gaps first (columns), then rows
        frac = sub.mean(axis=0 if axis == 1 else 1)
        cands = [r for r in runs(frac > 0.96) if 1 <= r[1] - r[0] <= 8]
        n = len(frac)
        cands = [r for r in cands if r[0] > MIN_AREA and n - r[1] > MIN_AREA]
        if cands:
            a, b = cands[0]
            if axis == 1:
                return split(m, [x0, y0, x0 + a, y1], depth + 1) + split(m, [x0 + b, y0, x1, y1], depth + 1)
            return split(m, [x0, y0, x1, y0 + a], depth + 1) + split(m, [x0, y0 + b, x1, y1], depth + 1)
    return [box]


def areas(path):
    img = Image.open(path)
    m = gap_mask(img)
    W, H = img.size
    boxes = split(m, content_box(img))
    out = []
    for x0, y0, x1, y1 in boxes:
        if x1 - x0 < MIN_AREA or y1 - y0 < 12:
            continue
        out.append({"box": [round(100 * x0 / W, 2), round(100 * y0 / H, 2), round(100 * (x1 - x0) / W, 2), round(100 * (y1 - y0) / H, 2)],
                    "px": [x0, y0, x1 - x0, y1 - y0]})
    return img, out


def overlay(img, found, dest):
    im = img.convert("RGB").copy()
    d = ImageDraw.Draw(im)
    for i, a in enumerate(found):
        x, y, w, h = a["px"]
        d.rectangle([x + 2, y + 2, x + w - 3, y + h - 3], outline=(255, 140, 0), width=6)
        d.text((x + 14, y + 10), str(i), fill=(255, 220, 0))
    im.thumbnail((1400, 900))
    im.save(dest)


if __name__ == "__main__":
    img, found = areas(sys.argv[1])
    if "--overlay" in sys.argv:
        overlay(img, found, sys.argv[sys.argv.index("--overlay") + 1])
    print(json.dumps(found))
