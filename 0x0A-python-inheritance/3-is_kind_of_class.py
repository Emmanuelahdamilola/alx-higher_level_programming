#!/usr/bin/python3
"""Defines the function"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the class, False otherwise.
    """
    if isinstance(obj, a_class):
        return True
    return False
