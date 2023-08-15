#!/usr/bin/python3
"""defines the method"""


def is_same_class(obj, a_class):
    """                                               Check if an object is exactly an instance of the specified class.                                   Args:                                                 obj: The object to be checked.
        a_class: The class to compare against.                                                          Returns:                                              True if the object is an instance of the specified class, False otherwise.
    """
    if (type(obj) == a_class):
        return True
    return False
