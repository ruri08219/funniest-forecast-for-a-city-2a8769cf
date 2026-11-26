"""Write the funniest weather forecast for a city that does not exist.

Deterministic, standard-library only: no network, no files outside this
repository, no randomness. Writes exactly one line (114 characters, no
trailing newline) to /output/entry.txt.
"""

import os

ENTRY = (
    "In Puddlewick, rain falls upwards all week; hold your umbrella "
    "underneath you and mind the puddles on the ceiling."
)


def validate(text):
    """The gate only accepts 1-120 characters of non-blank UTF-8 text."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry is blank")
    if len(cleaned) > 120:
        raise ValueError(f"entry is {len(cleaned)} characters, over the 120 limit")
    if cleaned != text:
        raise ValueError("entry has leading or trailing whitespace")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be exactly one line")
    return cleaned


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate(ENTRY))


if __name__ == "__main__":
    main()
