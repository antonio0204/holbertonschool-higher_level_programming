#!/usr/bin/python3

"BY: ronald"


def is_same_class(obj, a_class):
    """
    Arguments:
        obj {[type]} -- [description]
        a_class {[type]} -- [description]
    """
    if type(obj) == a_class:
        return True
    return False
