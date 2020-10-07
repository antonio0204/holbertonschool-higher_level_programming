#!/usr/bin/python3


"By: Ronald"


def inherits_from(obj, a_class):
    """Return True or False that inherited"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
