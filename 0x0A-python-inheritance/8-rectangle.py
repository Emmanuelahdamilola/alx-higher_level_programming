#!/usr/bin/python3
"""Defines a base class"""


class BaseGeometry:
    def area(self):
        """Calculates the area (to be implemented by subclasses)."""
        raise NotImplementedError("area() method not implemented")

    def integer_validator(self, name, value):
        """Validates that a value is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """Initializes a Rectangle with given width and height."""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
