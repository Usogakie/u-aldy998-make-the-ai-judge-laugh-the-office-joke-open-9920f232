"""Write one line of office comedy to entry.txt.

Deterministic: no network, no wall-clock, no randomness. The joke is a
fixed string, written to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt only.
"""

import os

JOKE = (
    "My calendar has started declining meetings on my behalf — "
    "honestly, its judgment is better than mine."
)


def main() -> None:
    # Gate the spek enforces: 1-200 chars, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke out of gate bounds"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
