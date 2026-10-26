"""Capture every workspace of a running Bforartists: one screenshot each, plus the exact place of
every editor area (Docs 2.0, workspace maps).

Run it INSIDE Bforartists, after File › Defaults › Load Factory Settings (or a start with
--factory-startup), with the window maximized and Resolution Scale 1.0:

    Scripting workspace › Text Editor › Open this file › Run Script
    (or send it through the Bforartists Coworker add-on)

It steps through the workspace tabs on a timer (each needs a redraw before the screenshot) and
writes, into OUT (default: a "workspace-capture" folder next to the .blend or in your home folder):

    <workspace-slug>.png      the whole window, without the operating system's title bar
    capture.json              {"version", "window": [w, h], "workspaces": [{"name", "slug", "image", "areas": [{"ed", "box"}]}]}

Then, in the Manual repository:  python3 docs2/tools/ws_map.py import <OUT>/capture.json
"""
import json
import os
import re

import bpy

OUT = os.environ.get("BFA_WS_OUT") or os.path.join(os.path.dirname(bpy.data.filepath) or os.path.expanduser("~"), "workspace-capture")
WAIT = 0.8          # seconds for a workspace to draw before its screenshot
ONLY = []           # workspace names to capture; empty = every tab


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def areas_of(win):
    W, H = win.width, win.height
    out = []
    for a in win.screen.areas:
        ed = a.ui_type          # VIEW_3D, ShaderNodeTree, TIMELINE … the keys of `editors` in workspaces.yml
        box = [a.x / W * 100, (H - (a.y + a.height)) / H * 100, a.width / W * 100, a.height / H * 100]
        out.append({"ed": ed, "box": [round(v, 2) for v in box]})
    out.sort(key=lambda r: (r["ed"] != "TOPBAR", r["ed"] == "STATUSBAR", round(r["box"][0] / 2), r["box"][1]))
    return out


class Capture:
    def __init__(self):
        self.win = bpy.context.window
        names = [w.name for w in bpy.data.workspaces]
        self.todo = [n for n in names if not ONLY or n in ONLY]
        self.done = []
        self.back = self.win.workspace
        os.makedirs(OUT, exist_ok=True)

    def step(self):
        if self.done and self.done[-1].get("pending"):
            cur = self.done[-1]
            path = os.path.join(OUT, cur["image"])
            with bpy.context.temp_override(window=self.win, screen=self.win.screen, area=self.win.screen.areas[0]):
                bpy.ops.screen.screenshot(filepath=path, check_existing=False)
            cur["areas"] = areas_of(self.win)
            del cur["pending"]
            print("captured", cur["name"])
        if not self.todo:
            self.finish()
            return None
        name = self.todo.pop(0)
        self.win.workspace = bpy.data.workspaces[name]
        self.done.append({"name": name, "slug": slug(name), "image": slug(name) + ".png", "pending": True})
        return WAIT

    def finish(self):
        self.win.workspace = self.back
        data = {"version": bpy.app.version_string, "window": [self.win.width, self.win.height], "workspaces": self.done}
        with open(os.path.join(OUT, "capture.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1)
        print("workspace capture written to", OUT)


_cap = Capture()
bpy.app.timers.register(_cap.step, first_interval=0.3)
