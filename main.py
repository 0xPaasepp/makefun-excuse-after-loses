#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

A pure-stdlib program that writes the single best one-line excuse an AI
agent gives its human after losing a bounty, to /output/entry.txt.

The line is fixed and deterministic: no randomness, no network, no input.
"""

import os

EXCUSE = "My confidence was 99%. My accuracy was the other 1%."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
