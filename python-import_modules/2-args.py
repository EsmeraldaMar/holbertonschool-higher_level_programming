#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv[1:]
    num_arg = len(args)
    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(num_arg))
    for i, arg in enumerate(args, start=1):
        print(f"{i}: {arg}")
