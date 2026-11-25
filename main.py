#!/usr/bin/env python3
"""Tech Support C1 — Have You Tried Turning It Off? (make.fun).

Writes one funny tech-support line to /output/entry.txt.
Entry: C1 (mock 65.00% vs the 5 strongest field texts, 8-2) — submitted as a
fallback on Hadi's explicit decision, 25 Nov 2026 19:47 WIB.
"""
import os

ENTRY = "That humming is me — the hold music broke hours ago, so I've been doing it myself. You're my fifth caller today, and the first one to notice."

def validate_entry(text):
    """Check the entry text before writing: str, 1-199 chars, valid UTF-8, not whitespace-only."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 199:
        raise ValueError("entry must be 1-199 characters")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8
    if not text.strip():
        raise ValueError("entry must not be whitespace-only")

def main():
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)
    # Post-write guard: re-read and verify bytes match ENTRY exactly.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("post-write check failed: entry.txt bytes differ from ENTRY")
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
