#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max = my_list[0]
    for nb in my_list:
        if max < nb:
            max = nb
    return max
