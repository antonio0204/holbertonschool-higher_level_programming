#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        if i is not 8:
            print("{}{}".format(i, j), end=", ")
        else:
            print("{}{}".format(i, j))