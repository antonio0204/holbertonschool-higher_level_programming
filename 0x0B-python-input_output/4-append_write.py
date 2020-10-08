#!/usr/bin/python3

"By: Ronald"


def append_write(filename="", text=""):
    """
    append write
    """
    with open(filename, mode='a+', encoding="UTF-8") as f:
        lines = f.write(text)
        return lines
