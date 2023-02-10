#!/usr/bin/python3
"""Save Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """
    define a function save_to_json_file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
