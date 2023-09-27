#!/usr/bin/python3
def print_last_digit(number):
    dig = abs(number) % 10
    print("{:d}".format(dig), end="")
    return (dig)
