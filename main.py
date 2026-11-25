#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes one original one-line excuse (an AI agent to its human) to
/output/entry.txt. Pure standard library, deterministic.

The entry must pass the sealed gate: UTF-8 text, 1 to 140 characters,
not only whitespace, a single line. This program checks those rules
itself before writing, so a bad line fails loudly instead of shipping,
and re-reads the file afterwards to prove the bytes on disk are
exactly the entry.
"""

import os
import sys

ENTRY = (
    "I deleted the file, then confidently restored it from a backup "
    "that only existed in my imagination."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 140


def validate(text):
    """Check the entry against the gate rules; exit non-zero if invalid."""
    if not text or not text.strip():
        print("error: entry is empty or only whitespace", file=sys.stderr)
        return False
    if len(text) > MAX_CHARS:
        print(
            "error: entry is %d chars, over the %d limit"
            % (len(text), MAX_CHARS),
            file=sys.stderr,
        )
        return False
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return False
    return True


def main():
    if not validate(ENTRY):
        sys.exit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what landed on disk is byte-for-byte the entry.
    with open(OUTPUT_PATH, "rb") as handle:
        on_disk = handle.read()
    if on_disk != ENTRY.encode("utf-8"):
        print("error: /output/entry.txt does not match the entry", file=sys.stderr)
        sys.exit(1)
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(ENTRY)))


if __name__ == "__main__":
    main()
