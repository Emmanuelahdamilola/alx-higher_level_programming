#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for character in str:
        if 'a' <= character <= 'z':
            uppercase_char = chr(ord(character) - 32)
            upper_str = upper_str + uppercase_char
        else:
            upper_str += character
    print(upper_str)
