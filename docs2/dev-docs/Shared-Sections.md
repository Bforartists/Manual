# ♻️ Shared sections

> **Write a section once. Every page that needs it shows the full text.**

Some menus and panels appear in many places (the Quick menu, the Marker menu). Instead of keeping 20 copies in step, the text lives in one file in `docs2/snippets/`, and each page points to it.

---

## 👀 What readers see

The full section, in place, on every page. Readers never follow a link to another chapter, so the [Reference Manual writing guide](https://github.com/Bforartists/Manual/wiki/Reference-Manual-writing-guide) rule still holds: *the information belongs in the entry*. Only writers see that it comes from one file.

---

## ✍️ What writers do

| Task | In Pages CMS | In a text editor |
|---|---|---|
| ➕ Show a shared section on a page | Pick it in the **Shared sections on this page** field | Add the path under `shared:` in the front matter, and the line `*Shared section: [Title](../snippets/file.md)*` where it should appear |
| ✏️ Change the shared text | Open **♻️ Shared snippets**, edit, Save | Edit the file in `docs2/snippets/` |
| 🆕 Make a new shared section | **♻️ Shared snippets** → **Add an entry** | Add a file in `docs2/snippets/` with the same front matter as a page |

One edit updates every page that shows the section.

---

## 🔎 Finding repeats

`docs2/tools/find_repeats.py` lists paragraphs that appear on several pages; `docs2/reports/repeats.json` holds the last run. These are candidates for new shared sections.

| Snippet today | Used on |
|---|---|
| `docs2/snippets/quick-menu.md` | Timeline header, and more as chapters migrate |
| `docs2/snippets/marker-menu.md` | Timeline header, and more as chapters migrate |
