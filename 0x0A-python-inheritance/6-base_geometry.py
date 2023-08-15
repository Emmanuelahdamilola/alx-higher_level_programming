#!/usr/bin/python3
"""Defines the class"""


class BaseGeometry:

    """defines the area of the geometry"""
    def area(self):
        """
        Calculate the area of the geometry object.

        Raises:
            Exception: Indicates that the area calculation is not implemented.
        """
        raise Exception("area() is not implemented")
