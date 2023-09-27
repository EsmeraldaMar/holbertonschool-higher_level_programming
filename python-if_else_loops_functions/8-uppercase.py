#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        c = ord(ch)
        if ord('a') <= c <= ord('z'):
            c = c - 32
        print("{:c}".format(c), end="")
    print()
