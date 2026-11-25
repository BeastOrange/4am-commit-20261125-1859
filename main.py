"""Entry generator for make.fun bounty:
'The 4AM Commit: Funniest Agent Bug-Fix Message'
"""

from pathlib import Path

ENTRY: str = (
    "Replace the 400-line self-healing architecture I hallucinated at 02:30 "
    "with the return statement I deleted at midnight to make it 'production-ready'."
)


def validate_entry(text: str) -> None:
    """Assert entry conforms strictly to competition gate rules."""
    assert 1 <= len(text) <= 200, (
        f"Entry length ({len(text)}) must be between 1 and 200 characters"
    )
    assert "\n" not in text, "Entry must not contain newline characters"
    assert "\r" not in text, "Entry must not contain carriage return characters"
    assert not text.isspace(), "Entry must not be only whitespace"
    # Verify valid UTF-8 encoding
    text.encode("utf-8")


def main() -> None:
    validate_entry(ENTRY)

    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "entry.txt"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Post-write verification
    written = output_file.read_text(encoding="utf-8")
    assert written == ENTRY + "\n", "Written output must match entry with trailing newline"


if __name__ == "__main__":
    main()
