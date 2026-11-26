#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single museum placard line for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt and prints it.
"""

LINE = (
    "Mouse, c. 1999. Moulded plastic. A hand-held idol, "
    "stroked daily by office priests to summon a cursor; "
    "the wheel turned, and nothing else moved. "
    "Gift of the IT department."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
