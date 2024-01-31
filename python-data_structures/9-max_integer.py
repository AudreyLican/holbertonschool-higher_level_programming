#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == "":
        return None

    max_value = my_list[0]
    for i in my_list:
        if max_value < i:
            max_value = i
    return max_value
