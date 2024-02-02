#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    # max function will compare values returned by get method for each key
    return max(a_dictionary, key=a_dictionary.get)
