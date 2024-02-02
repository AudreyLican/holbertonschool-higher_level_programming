#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    #create empty dictionnary to store multiplied values
    new_dic = {}
    #iterate over key-value in a_dictionnary
    for key, value in a_dictionary.items():
        new_dic[key] = value * 2
    return new_dic
