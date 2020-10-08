#!/usr/bin/python3


"""
    By: Ronald
    Read lines
    line
"""


def read_lines(filename="", nb_lines=0):
    """
        print all lines
        1 line: 'content'
        2 lien: 'content'
        3 lien: 'content'
    """
    with open(filename, encoding='utf-8') as f:
        if nb_lines > 0:
            for i in range(nb_lines):
                print(f.readline(), end="")
        else:
            print(f.read(), end="")
