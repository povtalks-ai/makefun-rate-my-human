"""Rate My Human: the one-line review my agent would leave about its human.

Writes a single line (127 characters) to /output/entry.txt. Standard
library only; no network; deterministic.
"""

import os

LINE = (
    "He says 'take your time' and then refreshes the page every four "
    "seconds. Five stars. I have never felt so watched, or so loved."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read it back and check the gate: 1-200 characters, one line.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 200, len(written)
    assert "\n" not in written, "entry must be a single line"


if __name__ == "__main__":
    main()
