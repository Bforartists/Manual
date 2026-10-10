#!/usr/bin/env python3
"""Find repeated sections across converted pages -> shared snippet candidates.

Splits every page into sections at H2/H3, fingerprints each section's text with
word 5-gram shingles, and reports pairs with Jaccard similarity >= 0.6.
Usage: find_repeats.py OUT_DIR > repeats.json
"""
import os, re, sys, json, itertools, collections

def sections(md, path):
    md = re.sub(r"^---.*?---\n", "", md, flags=re.S)
    parts = re.split(r"^(#{2,4} .+)$", md, flags=re.M)
    out = []
    for i in range(1, len(parts), 2):
        title = parts[i].lstrip("# ").strip()
        body = parts[i + 1]
        text = re.sub(r"!\[[^\]]*\]\([^)]*\)(\{[^}]*\})?", "", body)
        text = re.sub(r"[|*_:#`>\-\[\]{}()]", " ", text).lower()
        w = re.findall(r"[a-z0-9']+", text)
        if len(w) < 25: continue
        out.append({"page": path, "title": title, "level": len(parts[i]) - len(parts[i].lstrip("#")), "words": len(w),
                    "sh": {" ".join(w[j:j + 5]) for j in range(len(w) - 4)}})
    return out

root = sys.argv[1]
secs = []
for d, _, fs in os.walk(root):
    for f in fs:
        if f.endswith(".md"):
            p = os.path.join(d, f)
            secs += sections(open(p).read(), os.path.relpath(p, root))
pairs = []
for a, b in itertools.combinations(secs, 2):
    if a["page"] == b["page"] and a["title"] == b["title"]: pass
    inter = len(a["sh"] & b["sh"])
    if not inter: continue
    j = inter / len(a["sh"] | b["sh"])
    if j >= 0.6:
        pairs.append({"sim": round(j, 2), "a": f'{a["page"]} › {a["title"]}', "b": f'{b["page"]} › {b["title"]}',
                      "words": min(a["words"], b["words"])})
# group into clusters
parent = {}
def f(x):
    parent.setdefault(x, x)
    while parent[x] != x: x = parent[x]
    return x
for p in pairs: parent[f(p["a"])] = f(p["b"])
groups = collections.defaultdict(set)
for p in pairs: groups[f(p["a"])].update([p["a"], p["b"]])
wc = {f'{s["page"]} › {s["title"]}': s["words"] for s in secs}
res = []
for g in groups.values():
    g = sorted(g)
    words = [wc[x] for x in g]
    res.append({"members": g, "copies": len(g), "words_each": max(words), "words_saved": sum(words) - max(words)})
res.sort(key=lambda r: -r["words_saved"])
# drop clusters fully contained in a bigger cluster's sections (nested headings)
print(json.dumps({"sections_scanned": len(secs), "clusters": res,
                  "total_words_saved": sum(r["words_saved"] for r in res)}, indent=1))
