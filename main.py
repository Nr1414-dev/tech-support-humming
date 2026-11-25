#!/usr/bin/env python3
"""Tech Support C1 — Have You Tried Turning It Off? (make.fun).

Writes one funny tech-support line to /output/entry.txt.
Entry: C1 (mock 65.00% vs the 5 strongest field texts, 8-2) — submitted as a
fallback on Hadi's explicit decision, 25 Nov 2026 19:47 WIB.
"""
import os

ENTRY = "That humming is me — the hold music broke hours ago, so I've been doing it myself. You're my fifth caller today, and the first one to notice."

def main():
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
