"""One Emoji, One Smile — a single emoji chosen to make a stranger smile.

The entry is exactly one emoji, written to /output/entry.txt with no
words, no caption and no explanation, as the competition's gate requires.
"""

import sys
from pathlib import Path

EMOJI = "\U0001f970"

OUTPUT_PATH = Path("/output/entry.txt")


def entry_summary(text: str) -> dict:
    """Small report about the chosen emoji, for the run log only."""
    encoded = text.encode("utf-8")
    return {
        "characters": len(text),
        "utf8_bytes": len(encoded),
        "code_points": [f"U+{ord(ch):04X}" for ch in text],
        "is_single_emoji": len(text) == 1,
    }


def check_entry(text: str) -> None:
    """Enforce the competition gate: 1 to 8 UTF-8 characters, not blank."""
    if not text:
        raise ValueError("entry is empty")
    if len(text) > 8:
        raise ValueError("entry is longer than 8 characters")
    if text.strip() == "":
        raise ValueError("entry is only white space")


def main() -> int:
    check_entry(EMOJI)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EMOJI, encoding="utf-8")
    summary = entry_summary(EMOJI)
    print(f"wrote {EMOJI!r} ({summary['utf8_bytes']} bytes) to {OUTPUT_PATH}")
    print(f"summary: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
