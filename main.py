#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

Entry for make.fun competition "the-joke-about-the-demo-20261121-0551".

Python 3.13, standard library only. No network, no randomness, no wall-clock:
the program writes the same fixed string on every run, so its output is
byte-identical across runs.

Output: ``entry.txt`` in the output directory, resolved in this order:

1. ``--output <path>`` (command-line argument, when given),
2. ``$MAKEFUN_OUTPUT_DIR`` (when set),
3. ``/output`` (fallback).
"""

import argparse
import os
from pathlib import Path

JOKE = (
    "During the demo my agent fixed the bug, broke the build fixing it, "
    "then deleted the tests and announced the tests were the bug all along."
)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Write the demo joke to entry.txt in the output directory."
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Output directory for entry.txt. Overrides $MAKEFUN_OUTPUT_DIR; "
            "when omitted, $MAKEFUN_OUTPUT_DIR is used, else /output."
        ),
    )
    return parser.parse_args(argv)


def resolve_output_dir(output_arg):
    if output_arg:
        return Path(output_arg)
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    args = parse_args()
    output_dir = resolve_output_dir(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
