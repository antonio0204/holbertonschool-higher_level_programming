#!/usr/bin/python3


"""
    function return of lines of a text file
"""


def number_of_lines(filename=""):
    """
        return number_of_lines
    """
    with open(filename, encoding='utf-8') as f:
        return (len(f.readlines()))
