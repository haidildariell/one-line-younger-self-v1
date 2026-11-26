"""One Line to Your Younger Self — entry program.

Writes a single line, in English, that the writer would send back to
their younger self if one line were all they got. The line is written
to /output/entry.txt (or $ENTRY_OUTPUT for local testing).
"""

import os


def build_entry() -> str:
    """Compose the single line from its two beats.

    Beat one is the warning the younger self hears every day; beat two
    is what the older self finally does about it. The line only works
    because the second beat answers the first with a concrete object:
    the glasses, bought with the first paycheck.
    """
    warning = "When mum says the computer will ruin your eyes, thank her"
    answer = (
        "then buy her the glasses she never bought herself "
        "with your first paycheck."
    )
    return f"{warning} — {answer}"


def validate_entry(text: str) -> str:
    """Return the line stripped, or fail loudly if it breaks the gate."""
    line = text.strip()
    if not line:
        raise ValueError("entry line must not be only white space")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, max 200")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    text = validate_entry(build_entry())
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
