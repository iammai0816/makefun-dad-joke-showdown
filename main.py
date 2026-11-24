#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt.

The program is deterministic: it always emits the same single joke,
the entry itself, into entry.txt under MAKEFUN_OUTPUT_DIR.
"""

import os

JOKE = (
    "I told my son I keep the car keys in the freezer now. He asked why. "
    "I said, 'So we can chill before we drive.'"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
