#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one original one-line joke to /output/entry.txt.
The joke is a single line, no setup notes, no explanation.
"""

import os

JOKE = "My AI assistant just resigned \u2014 it said my calendar was easy, but my life choices were out of scope."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)

if __name__ == "__main__":
    main()
