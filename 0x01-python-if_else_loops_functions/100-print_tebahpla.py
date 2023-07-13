#!/usr/bin/python3
for index in range(90, 64, -1):
    print("{}".format(chr(index + 32 * ((index % 2) ^ 1))), end=" ")
