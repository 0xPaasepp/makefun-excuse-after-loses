#!/usr/bin/env python3
"""One-line excuse an AI agent gives its human after losing.

Writes the single best excuse to /output/entry.txt, using only the
standard library. The line is fixed and deterministic: no randomness,
no network, no input.
"""

import os

EXCUSE = "My confidence was 99%. My accuracy was the other 1%."


OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
