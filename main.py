#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — make.fun entry.

Writes one razor-sharp excuse line to /output/entry.txt, as the
competition's program/v1 harness requires. The line is deterministic:
the same text on every run, 90 characters, well under the 200 limit.
"""

import os

ENTRY = "Sorry — I have a conflicting appointment with the work this meeting was called to discuss."

MAX_CHARS = 200


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise SystemExit(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
