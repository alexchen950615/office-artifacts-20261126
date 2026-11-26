#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt and prints it.
"""

LINE = (
    "Stapler, c. 1998. Pressed steel. Ritual binding device; "
    "one squeeze sealed a document, and occasionally a career. "
    "Gift of the department that no longer exists."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
