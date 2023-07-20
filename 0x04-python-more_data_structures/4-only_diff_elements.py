#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_1_o = set_1.difference(set_2)
    set_2_o = set_2.difference(set_1)
    return set_1_o.union(set_2_o)
