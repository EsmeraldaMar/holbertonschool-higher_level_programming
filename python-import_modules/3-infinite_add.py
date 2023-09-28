#!/usr/bin/python3
import sys
if __name__ == "__main__":
    result = 0
    args = sys.argv[1:]
    for i, arg in enumerate(args, start=0):
        result += int(args[i])
    print("{:d}".format(result))
