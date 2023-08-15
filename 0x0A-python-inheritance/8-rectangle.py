#!/usr/bin/python3


class BaseGeometry:
    """
    Defines BaseGeometry class
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is an integer greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Instantiating with width and height
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height
