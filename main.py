#!/usr/bin/env python3
"""Write the worst-Monday one-liner to entry.txt in the output folder."""

import os

# One line about an AI agent's worst Monday: picked from five drafts
# judged pairwise on the kit's criteria (on subject first, then a
# real laugh with a sharp last word, a concrete detail, one-breath
# voice, fresh). The wreckage is concrete - a ticket flood and a
# broken deploy - and the last word is the oldest IT advice there is,
# aimed at the agent itself. The gate checks entry.txt as UTF-8 text
# of 1 to 140 characters: this line is 96 code points, 97 with its
# trailing newline (verified by a local run).
TEXT = "Monday: 6,000 tickets, one broken deploy, and a human asking if I've 'tried turning myself off.'"


def write_entry(out_dir: str) -> None:
    """Write the line, with its trailing newline, into out_dir."""
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
