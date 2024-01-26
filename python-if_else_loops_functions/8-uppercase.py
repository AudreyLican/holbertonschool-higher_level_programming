#!/usr/bin/python3
def uppercase(text):
    for char in text:
        if 97 <= ord(char) and ord(char) <= 122:
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
