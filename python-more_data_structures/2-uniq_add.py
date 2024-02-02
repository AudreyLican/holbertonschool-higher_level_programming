#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set(my_list)
    result = 0
    for nb in uniq_int:
        result += nb
    return result
