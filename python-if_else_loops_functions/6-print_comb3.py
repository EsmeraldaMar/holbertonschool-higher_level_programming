#!/usr/bin/python3
for first in range(0, 10):
    for second in range(0, 10):
        if first != second and second > first:
            if first == 8:
                print("{:d}{:d}".format(first, second))
            else:
                print("{:d}{:d}, ".format(first, second), end="")
