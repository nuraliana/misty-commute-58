"""One-line office joke entry.

Writes the entry text to entry.txt inside the directory named by
MAKEFUN_OUTPUT_DIR. Standard library only, deterministic, no network.
"""

import os
import sys

ENTRY = "I work from home three days a week and come to the office to video-call the people working from home."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
