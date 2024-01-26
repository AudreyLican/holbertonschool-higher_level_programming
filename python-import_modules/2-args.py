#!/usr/bin/python3
import sys

def main():
    args_num = len(sys.argv) - 1
    if (args_num == 0):
        print("0 arguments.")
    elif (args_num == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(args_num))
    for arg in range(1, len(sys.argv)):
        print("{}: {}".format(arg, sys.argv[arg]))

if __name__ == "__main__":
    main()
