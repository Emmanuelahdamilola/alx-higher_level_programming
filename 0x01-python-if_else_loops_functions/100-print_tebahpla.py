#!/usr/bin/python3
for index in range(90, 64, -1):
    print("{:c}".format(index + 32 * ((index % 2) ^ 1)), end=" ")
