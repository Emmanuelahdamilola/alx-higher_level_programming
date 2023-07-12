#!/usr/bin/python3
for ascii_alp in range(97, 123):
    if (chr(ascii_alp) not in ["q", "e"]):
        print("{}".format(chr(ascii_alp)), end='')
