#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if (i != j and i < j) and i <  9:
            if (i != 8 or j != 9):
                print("{}{}".format(i, j), end=", ")
            else:
                print("{}{}".format(i, j))
