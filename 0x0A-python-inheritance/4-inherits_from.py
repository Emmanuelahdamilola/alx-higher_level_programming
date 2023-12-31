#!/usr/bin/python3
"""Defines the subclass function"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly) from a class.

    Args:
        obj: The object to be checked.
        a_class: The specified class to check against.

    Returns:
        True if the object is an instance of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
