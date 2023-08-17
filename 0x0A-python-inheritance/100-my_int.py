#!/usr/bin/python3
"""Defines a class MyInt """


class MyInt(int):
    """Inverts the equal to """
    def __eq__(self, value):
        """Overrides equal to operator with not equal to operator"""
        return self.real != value

    def __ne__(self, value):
        """Overrides not equal to with equal to operator"""
        return self.real == value
