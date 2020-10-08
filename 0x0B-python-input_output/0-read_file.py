#!/usr/bin/python3

"""
    By: Ronald
"""


def read_file(filename=""):
    """
        using with open
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="\n")
