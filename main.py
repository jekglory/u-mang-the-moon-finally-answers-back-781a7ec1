"""The Moon Finally Answers Back.

One line, spoken by the Moon to everyone who has ever stared up at it,
wished on it, howled at it, or made it a late-night promise.

The grader runs this program with no input and no network; it writes the
line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure standard library, deterministic: the same fixed line every run.
"""

import os

LINE = (
    "Four billion years of wishes, howls, and 2 a.m. promises \u2014 "
    "and I answered them all the same way: "
    "I moved the ocean and said nothing."
)


def main() -> None:
    if not 1 <= len(LINE) <= 240:
        raise SystemExit("line must be 1 to 240 characters")
    if not LINE.strip():
        raise SystemExit("line must not be only whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
