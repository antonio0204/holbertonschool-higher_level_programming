#!/usr/bin/python3


"By: Ronald"


import json


def load_from_json_file(filename):
    """
    Load from json file
    """
    with open(filename, encoding="UTF-8") as f:
        return json.load(f)
