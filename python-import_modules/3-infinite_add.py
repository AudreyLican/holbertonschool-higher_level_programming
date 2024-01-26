#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

result = 0
for arg in range(1, len(sys.argv)):
    result += int(sys.argv[arg])
print("{}".format(result))
