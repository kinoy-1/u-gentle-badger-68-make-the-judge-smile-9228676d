#!/usr/bin/env python3
"""u-gentle-badger-68-make-the-judge-smile-9228676d: write one warm line to /output/entry.txt.

The line is the whole entry: one sentence, 129 characters, built for the
judge's criteria in order.

1. A small good thing that happened today, one that makes the judge smile:
   a neighbour left a tomato on my doorstep with a kind note.
2. Warmth: a small kindness that lands as genuinely felt -- someone noticed
   I was hungry and acted on it, without being asked.
3. Surprise, saved for the very end: "I hadn't told a soul I'd skipped
   lunch" -- how did the neighbour know? The turn reframes the whole
   sentence once it arrives.
4. Concreteness: one real small detail -- a tomato, a doorstep, a quoted
   note -- rather than a general sentiment.
5. Fresh wording: plain spoken words, no greeting-card phrasing, no
   borrowed sentiment.

It runs offline, standard library only, and writes the same bytes on
every run.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The winning line, written for the judge's criterion #1 first:
# a small good thing today, with the surprise saved for the very end.
LINE = (
    "Today a neighbour left a tomato on my doorstep "
    "\u2014 'grew too many, you looked hungry' \u2014 "
    "and I hadn't told a soul I'd skipped lunch."
)

# Gate: the judge scores only lines of 1-200 characters, one line.
# Validated at run time so a future edit to the line can never
# silently break it -- a bad line fails loudly instead of submitting.
def validate_line(line: str) -> str:
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"line must be 1-200 characters, got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only white space")
    return line


def main() -> None:
    line = validate_line(LINE)
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
