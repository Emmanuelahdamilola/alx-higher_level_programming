#!/usr/bin/python3
def pow(a, b):
    result = 1

    if (b == 0):
        return 1

    if (b > 0):
        for x in range(b):
            result = result * a
    else:
        for x in range(-b):
            result = result * a
        result = 1 / result

    return result
