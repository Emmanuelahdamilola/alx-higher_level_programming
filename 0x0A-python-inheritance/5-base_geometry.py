#!/usr/bin/python3

class BaseGeometry:
    """
    An empty class representing a base geometry.
    """
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError
