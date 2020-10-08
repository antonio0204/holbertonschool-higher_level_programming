#!/usr/bin/python3


"""By: Ronald
"""


import json
import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    list_new = load_from_json_file(filename) + sys.argv[1:]
except Exception:
    list_new = sys.argv[1:]

save_to_json_file(list_new, filename)
