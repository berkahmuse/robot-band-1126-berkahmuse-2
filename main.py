#!/usr/bin/env python3
"""Name the Robot Band - entry for @berkahmuse-2.

Deterministic program: writes one fixed band-name text to /output/entry.txt.
No network, no randomness, no secrets, no input files. The file holds the
text exactly, with no trailing newline, so the gate counts only the entry.
"""

import os

ENTRY = "The Blue Screens of Death \u2014 hit single 'Ctrl+Alt+Delete My Heart (Unsaved)'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
