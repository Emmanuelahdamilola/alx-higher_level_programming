#!/usr/bin/python3
def magic_string():
    magic_string.count = getattr(magic_string, "counter", 0) + 1
    return "BestSchool" * magic_string.count
