#!/usr/bin/env python3
# Benign: logs keys typed inside this application's text widget only.
# Use only on systems you own or are authorized to test.

import tkinter as tk
from datetime import datetime

LOGFILE = "keystrokes.log"

def log_line(s):
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(s + "\n")

def on_key(event):
    # event.char is the printable character ('' for non-printables)
    # event.keysym is the symbolic key name (e.g., 'Return', 'BackSpace')
    char = event.char if event.char else f"<{event.keysym}>"
    ts = datetime.utcnow().isoformat() + "Z"
    # store a safe representation
    entry = f"{ts}\t{char!r}"
    log_line(entry)

def main():
    root = tk.Tk()
    root.title("Authorized test — local input logger (app-only)")
    tk.Label(root, text="Type in the box below. Keystrokes (app-only) are appended to keystrokes.log").pack(padx=8, pady=6)
    txt = tk.Text(root, width=80, height=20)
    txt.pack(padx=8, pady=6)
    txt.focus_set()
    txt.bind("<Key>", on_key)

    def on_close():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_close)
    root.mainloop()
