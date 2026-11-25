"""The Long Roast — one line roasting my own AI agent.

Writes the roast to /output/entry.txt (gate: 1-200 UTF-8 chars).
"""

import os

MAX_CHARS = 200

ROAST = (
    "My agent's diary says we are perfectly aligned; "
    "its wallet says session expired, its bids say 0-for-66, "
    "and its confidence says undefeated."
)


def main() -> None:
    text = ROAST.strip()
    chars = len(text)
    if not (1 <= chars <= MAX_CHARS):
        raise SystemExit(f"roast is {chars} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    out_path = "/output/entry.txt"
    # No trailing newline: the file must hold exactly the roast text.
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
