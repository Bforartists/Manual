# Webflow 301 redirects for the old documentation

## Go-live checklist (October 2026 clean-up)

1. ✅ Links on the marketing pages, the footer, the 404 page and the Docs template point at `/docs/…` (rewired on staging).
2. ✅ The 97 old `/documentation/…` pages are set to **Draft** in Webflow (reversible: untick Draft in Page settings).
3. ⬜ Add the 41 redirects below in Webflow: Site settings › Publishing › 301 redirects.
4. ⬜ Publish the live site, then open a few old addresses (for example `/documentation/keymap/standard`) and check they land on the new page.
5. ⬜ After a week or two, delete the old pages and their folders in the Designer (Pages panel › `documentation` folder).

Add in Webflow: Site settings › Publishing › 301 redirects. **Exact rules first** (Webflow uses the first rule that matches), then the patterns. Generated from `legacy-redirects.csv` (97 old pages, every one checked against the new sidebar).

## Exact rules

| Old path | Redirect to |
|---|---|
| `/documentation` | `/docs/home` |
| `/documentation/advanced` | `/docs/advanced` |
| `/documentation/advanced/command-line` | `/docs/advanced-advanced-command-line` |
| `/documentation/advanced/scripting` | `/docs/advanced-advanced-scripting-extending-bforartists` |
| `/documentation/advanced/working-limits` | `/docs/advanced-advanced-working-limits` |
| `/documentation/appendix/chapters` | `/docs/appendix-index-a-z` |
| `/documentation/appendix/documentation-history` | `/docs/appendix-manual-update-history` |
| `/documentation/appendix/history` | `/docs/appendix-bforartists-history` |
| `/documentation/assets` | `/docs/assets` |
| `/documentation/development/compiling-on-windows` | `https://github.com/Bforartists/Bforartists/wiki` |
| `/documentation/development/doing-documentation` | `https://github.com/Bforartists/Manual/wiki` |
| `/documentation/editors` | `/docs/editors` |
| `/documentation/editors/nonlinear-animation` | `/docs/editors-nonlinear-animation-editor` |
| `/documentation/editors/properties-editor` | `/docs/editors-properties` |
| `/documentation/editors/status-bar` | `/docs/editors-topbar-and-statusbar` |
| `/documentation/editors/tool-bar-editor` | `/docs/editors-toolbar` |
| `/documentation/editors/top-bar` | `/docs/editors-topbar-and-statusbar` |
| `/documentation/editors/video-sequencer` | `/docs/editors-video-sequence-editor` |
| `/documentation/extensions` | `/docs/extensions` |
| `/documentation/information` | `/docs/appendix` |
| `/documentation/interface` | `/docs/interface` |
| `/documentation/interface/headers` | `/docs/interface-header` |
| `/documentation/interface/interface` | `/docs/interface-basics` |
| `/documentation/interface/properties` | `/docs/interface-controls` |
| `/documentation/interface/side-bars` | `/docs/interface-sidebar` |
| `/documentation/interface/tabs-panels` | `/docs/interface-panels-and-tabs` |
| `/documentation/interface/tool-shelves` | `/docs/interface-tool-shelf` |
| `/documentation/keymap` | `/docs/keymap` |
| `/documentation/keymap/important` | `/docs/keymap-important-hotkeys` |
| `/documentation/keymap/standard` | `/docs/keymap-standard-keymaps` |
| `/documentation/overview` | `/docs/getting-started` |
| `/documentation/workspaces` | `/docs/workspaces` |

## Pattern rules

| Old path | Redirect to |
|---|---|
| `/documentation/assets/geometry-nodes/(.*)` | `/docs/assets` |
| `/documentation/advanced/(.*)` | `/docs/advanced-%1` |
| `/documentation/appendix/(.*)` | `/docs/appendix-%1` |
| `/documentation/assets/(.*)` | `/docs/assets-%1` |
| `/documentation/editors/(.*)` | `/docs/editors-%1` |
| `/documentation/interface/(.*)` | `/docs/interface-%1` |
| `/documentation/keymap/(.*)` | `/docs/keymap-%1` |
| `/documentation/overview/(.*)` | `/docs/getting-started-%1` |
| `/documentation/workspaces/(.*)` | `/docs/workspaces-%1` |
