#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes the single Monday-morning joke from joke.txt to
/output/entry.txt, where the sealed scorer reads it. The joke is kept
in joke.txt so the text lives in one obvious place; this script only
checks it fits the gate (one line, 1-200 characters, not blank) and
copies it out.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
JOKE_FILE = os.path.join(HERE, "joke.txt")
MAX_CHARS = 200


def read_joke():
    with open(JOKE_FILE, encoding="utf-8") as handle:
        content = handle.read()
    line = content.strip("\n")
    if not line.strip():
        raise ValueError("joke.txt is empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line")
    if line != line.strip():
        raise ValueError("joke has leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(f"joke is {len(line)} chars, over the {MAX_CHARS} limit")
    return line


def main():
    joke = read_joke()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke + "\n")
    print(f"wrote {len(joke)}-character joke to {out_path}")
    print(joke)


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
