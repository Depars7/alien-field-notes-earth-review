"""Write the alien field-notes entry to /output/entry.txt.

Gate (from RULES.txt): /output/entry.txt is UTF-8 text of 1 to 200
characters, not only white space, one line: a one-line review of
planet Earth by an alien tourist.
"""

import os

PARTS = (
    "★★★★☆. ",
    "The locals apologize to furniture when they bump into it ",
    "and queue in silence to be judged by glowing rectangles. ",
    "Docked one star: nobody offered the visitor a chair.",
)


def entry_line():
    return "".join(PARTS)


def main():
    os.umask(0o022)
    line = entry_line()
    assert 1 <= len(line) <= 200, "entry must be 1 to 200 characters"
    assert line.strip(), "entry must not be only white space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    line.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
