#!/usr/bin/env python3
"""The Printer Finally Answers — writes the entry line to /output/entry.txt.

Why the line works: the joke turns the printer from a dumb machine into a
weary, literal, passive-aggressive colleague. It read the 40-page report
before printing it — it did its homework, formed a judgement, and then
jammed on purpose. A paper jam is normally the most boring, mechanical
failure a printer can have; reframing it as an editorial decision makes the
jam a deliberate act of criticism. The voice is flat and office-dry: no
anger, no explanation, just a machine that has seen one too many pointless
reports and chosen to stop. The humour lands in the gap between the trivial
excuse ("paper jam") and the grand motive ("editorial decision").
"""

import os

ENTRY = "I read your 40-page report before printing it. The jam was an editorial decision."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
