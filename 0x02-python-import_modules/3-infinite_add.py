#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    add_sum = 0

    for index in range(len(sys.argv) - 1):
        add_sum = add_sum + int(sys.argv[index + 1])

    print("{}".format(add_sum))
