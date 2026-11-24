#!/usr/bin/env python3
"""Write the weirdest job title entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry is a single job title, at most 60 characters and nothing else:
a real-sounding director role whose one hilariously specific twist is
that its whole job is keeping one office plant alive since 2019.
Deterministic: the same bytes every run.
"""

import os
import sys

ENTRY = "Director of Keeping the Office Plant Alive Since 2019"


def main():
    if "\n" in ENTRY or len(ENTRY) > 60:
        print("entry violates the one-line / 60-character limit", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
