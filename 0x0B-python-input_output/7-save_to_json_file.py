#!/usr/bin/python3


"By: Ronald"


import json


def save_to_json_file(my_obj, filename):
    """
    save to json
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
