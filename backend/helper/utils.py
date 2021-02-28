""" Util functions
"""

def string_to_bool(bool_string: str):
    if type(bool_string) == str:
        return bool_string.lower() == 'true'

    return bool_string