#!/usr/bin/env python3
"""Museum of the Year 3000 — make.fun bounty entry.

Writes a single museum label (one line, <=200 chars, English) to
/output/entry.txt: the label a museum in the year 3000 puts beside an
ordinary object from today.
"""

import os

ENTRY = (
    "Group Chat, c. 2025. Seventeen humans shared a single conversation "
    "for nine years. Fourteen of them never spoke. "
    "All seventeen read everything."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
