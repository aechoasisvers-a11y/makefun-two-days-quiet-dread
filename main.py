"""Write the Two Days of Quiet Dread entry to /output/entry.txt.

Pure stdlib, deterministic: the same single-line code review comment
every run, with no trailing newline.
"""

import os

ENTRY_TEXT = (
    "LGTM. Clean diff, green tests, and the quiet certainty "
    "this code will outlive us both."
)


def main() -> None:
    # Self-check (pass 2): the brief's gate, enforced before writing.
    # Single line, approves the PR ("LGTM"), carries quiet dread,
    # 1-140 characters, not only whitespace, no trailing newline.
    assert 1 <= len(ENTRY_TEXT) <= 140, f"entry is {len(ENTRY_TEXT)} chars"
    assert "\n" not in ENTRY_TEXT and "\r" not in ENTRY_TEXT, "entry must be one line"
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "LGTM" in ENTRY_TEXT, "entry must approve the pull request"
    assert not ENTRY_TEXT.endswith("\n"), "no trailing newline"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)

    # Verify what was actually written matches the intended text exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY_TEXT, "written output differs from intended entry"
    assert 1 <= len(written) <= 140, "written output outside the char gate"


if __name__ == "__main__":
    main()
