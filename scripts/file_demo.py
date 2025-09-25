"""Simple file read/write practice script.

Creates a demo text file, appends a line, then reads it back.
"""
from __future__ import annotations
from pathlib import Path

DATA_FILE = Path(__file__).parent / "demo_data.txt"


def write_initial():
    DATA_FILE.write_text("Line 1: Hello file!\n", encoding="utf-8")


def append_line(line: str):
    with DATA_FILE.open("a", encoding="utf-8") as f:
        f.write(line.rstrip("\n") + "\n")


def read_all() -> list[str]:
    return DATA_FILE.read_text(encoding="utf-8").splitlines()


def main():
    if not DATA_FILE.exists():
        write_initial()
        append_line("Line 2: First append.")
    else:
        append_line("Another line appended.")

    for i, line in enumerate(read_all(), 1):
        print(f"{i:02d}: {line}")


if __name__ == "__main__":
    main()
