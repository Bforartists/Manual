# 📐 Formatting standard

> **One shape for every page, so readers always know where to look and writers never have to guess.**

These rules come from the maintainer's reviews and from an audit of all 333 pages (see the [consistency plan](../plans/plan_docs2_consistency_and_components.md)). Pages that do not follow them yet are fixed in small PRs, one chunk at a time.

---

## 🧱 The page skeleton

| Level | Used for |
|---|---|
| `#` | The region or the page title (one per region) |
| `##` | A menu, panel or major area |
| `###` | A group of related entries |
| `####` | **One operator, tool or entry** |
| `#####` | Its parts: Inputs, Properties, Outputs, Adjust Last Operation, panel groups |
| `######` | A single property inside those parts |

- Never skip a level (`##` straight to `####`).
- Never use bold text as a stand-in for a heading.

---

## 🖱️ Operators and tools

**Every operator is a sub-heading**, followed by its explanation. Never in bold inside a paragraph, never a table row.

Each one has the same three parts, in this order:

1. 🏷️ **Heading**: the name exactly as the UI shows it.
2. 📝 **A short tooltip-style explanation**: what it is, why you would use it, how it works. Plain words.
3. 🖼️ **A capture**: the menu, panel or result, taken in place.

Cluster a few closely related operators under one heading with one shared capture when that reads better.

---

## 🔁 Adjust Last Operation

The panel that appears after you run an operator. Every operator that has one gets a section **under its own heading**:

```
#### Move
(explanation + capture of the operator)

##### Adjust Last Operation
(one sentence: what the panel changes)
(capture of the panel, in place)
| Property | What it changes |
```

- The heading is always **Adjust Last Operation** (the name the UI uses), not "Last Operator Move".
- It always has **a heading, a sentence and a capture**.
- This is the **only place a table is welcome**: the properties of the panel.
- Properties that many operators share (Proportional Editing, Orientation, Mirror Editing) are described once on the [Last Operator panel](../content/interface/last-operator-panel.md) page. The operator lists only its own properties and links to the shared ones.

---

## 🔌 Node pages

Nodes already follow the pattern everyone should use. Keep it:

```
#### Node name
(capture + explanation)

##### Inputs
###### Each input
##### Properties
###### Each property
##### Outputs
###### Each output
```

- The order is always **Inputs, Properties, Outputs**. A section is left out when the node has none.
- Each input, property and output is its own heading with a short explanation. No tables.

---

## 📊 Tables

Tables are for **data that really is a grid**: keymaps, a list of hotkeys, the properties of an Adjust Last Operation panel. Entries, operators and settings are never tables.

---

## 🖼️ Pictures

- Capture panels **in place** in the real editor. Never as a floating popup.
- Normal editor width, about 400 to 800 px.
- When an entry changes, update the **overview picture** (the whole menu or panel) too.
- A page with no picture needs a reason.

---

## ♻️ Things that appear in many places

Two tools exist; see the plan for when to use which:

- **Concept** (what proportional editing is, how the curve widget works): one page in the Interface chapter. Editor pages keep a short callout, a capture of their own variant, and a link.
- **Identical panel** (the Quick menu, the Marker menu): a [shared section](Shared-Sections.md). The full text shows in place.

Never copy a paragraph between pages. If you need it twice, make it one of the two above.

---

## ✅ Quick checklist for a PR

- [ ] Every operator has its own sub-heading, explanation and capture
- [ ] No skipped heading levels, no bold lines used as headings
- [ ] Tables only for Adjust Last Operation properties or real data grids
- [ ] Overview pictures updated if an entry changed
- [ ] `python3 docs2/tools/check.py .` passes
