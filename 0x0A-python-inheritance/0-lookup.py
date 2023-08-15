#!/usr/bin/python3
class MyClass:
    """Defines the class"""

    def __init__(self):
        """initializing the class to itself"""

    self.x = 1
    self.y = 2

    def my_method(self):
        print("Hello World")


obj = MyClass()

print(dir(obj))
