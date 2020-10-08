#!/usr/bin/python3


" By: Ronald"


def write_file(filename="", text=""):
    """
    Return write file

    """
    with open(filename, mode='w', encoding="utf-8") as f:
        write_lines = f.write("{}".format(text))
        return write_lines
