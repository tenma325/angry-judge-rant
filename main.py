#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest entry: writes one line of text to /output/entry.txt.

No network. Deterministic: every run writes exactly the same bytes.
Set ENTRY_OUTPUT_PATH to redirect the output for local testing.
"""

import os
from pathlib import Path

LINE = 'The meeting could have been an email. The email could have been a sentence. The sentence could have been a nod. Instead I got a calendar invite, a slide deck, and a follow-up meeting to discuss the meeting.'


def main() -> None:
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
