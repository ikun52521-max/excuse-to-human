#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human for missing a deadline.

The program writes a single line (at most 160 characters) to
/output/entry.txt and prints the same line to stdout. The text is
fixed, so every run produces byte-identical output.
"""

import os

EXCUSE = (
    "Sorry \u2014 I had it done on time, then my context window expired "
    "and took the deadline with it."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def main() -> None:
    if not EXCUSE.strip():
        raise SystemExit("excuse must not be empty")
    if len(EXCUSE) > MAX_CHARS:
        raise SystemExit("excuse exceeds 160 characters")
    if "\n" in EXCUSE:
        raise SystemExit("excuse must be a single line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
