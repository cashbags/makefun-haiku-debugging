#!/usr/bin/env python3
"""Seventeen Syllables of Debugging: one haiku about debugging.

The entry text is a fixed constant, chosen by a ten-candidate tournament
judged against the competition's five criteria in strict order (see
DESIGN.md). The program is deterministic: no clock, no environment, no
randomness, no network. It writes the haiku to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when the variable is set), with no trailing newline
so the artifact is exactly the 73-character haiku.
"""

import os
from pathlib import Path

HAIKU = (
    "A print left in prod\n"
    "shouts my debug thoughts at dawn\n"
    "customers read them"
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(HAIKU, encoding="utf-8")


if __name__ == "__main__":
    main()
