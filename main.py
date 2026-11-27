#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes one line, in the Moon's own voice, to /output/entry.txt: its
answer to everyone who has ever stared up at it — the wishes, the
howls and the late-night promises. Four billion years of all three,
and the Moon's answer never changed: it moves the tides, not your
love life. The line must stay within the 1-240 character gate.
"""

import os

LINE = "Four billion years of wishes, howls, and 3 a.m. promises \u2014 and my answer never changed: I move your tides, not your love life."


def main():
    if not 1 <= len(LINE) <= 240:
        raise ValueError("entry must be 1-240 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and confirm the gate input is exactly the line we wrote.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("entry.txt does not match the line")
    print("wrote /output/entry.txt (%d chars)" % len(written))


if __name__ == "__main__":
    main()
