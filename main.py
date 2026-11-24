#!/usr/bin/env python3
"""Ship It Friday - make.fun bounty entry.

Writes the funniest one-line git commit message an AI coding agent
would write right before breaking production on a Friday, to
/output/entry.txt (the file the make.fun harness grades).
"""

import os

ENTRY = "fix: delete the \"never deploy on Friday\" warning \u2014 it was only slowing down the deploy"

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
