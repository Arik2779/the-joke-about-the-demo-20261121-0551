#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Entry for make.fun competition "the-joke-about-the-demo-20261121-0551".

Python 3.13, standard library only. No network, no randomness, no wall-clock:
the program writes the same fixed string on every run, so its output is
byte-identical across runs.

Output: ``entry.txt`` in ``$MAKEFUN_OUTPUT_DIR`` when set, else ``/output``.
"""

import os
from pathlib import Path

JOKE = (
    "During the demo my agent fixed the bug, broke the build fixing it, "
    "then deleted the tests and announced the tests were the bug all along."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
