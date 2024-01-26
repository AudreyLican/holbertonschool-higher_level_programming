#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if "a" <= char <= "z":
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

print(uppercase("best"))
print(uppercase("Best School 98 Battery street"))
