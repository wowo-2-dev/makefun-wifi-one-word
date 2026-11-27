"""One Word for Your Wi-Fi — make.fun bounty
Slug: u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72
Prize: $2, deadline Sat 28 Nov 2026 18:35 WIB (28 Nov 2026 11:35 UTC)
Limit: exactly one word (sealed gate: UTF-8 text of 1 to 20 characters,
not only white space)

Writes the entry text to /output/entry.txt (override with ENTRY_OUTPUT
for local testing). Deterministic, no network, no randomness, no I/O
other than the single output file. The file is exactly the entry text,
no trailing newline.

Why "liar": home Wi-Fi promises full bars and then drops mid-call — the
one word everyone recognises the moment they read it. Short, concrete,
true at once, no explanation needed.
"""

import os
from pathlib import Path

TEXT = 'liar'  # 4 characters, 1 word — inside the sealed 1-20 gate.


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(TEXT, encoding="utf-8")
    print(TEXT)


if __name__ == "__main__":
    main()
