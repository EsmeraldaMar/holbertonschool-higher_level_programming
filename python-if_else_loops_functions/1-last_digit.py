#!/usr/bin/python3
"""Module providing a function printing python version."""
import random
number = random.randint(-10000, 10000)
dig = number % 10
if number < 0:
    dig = number % -10
if dig > 5:
    print(f"Last digit of {number} is {dig} and is greater than 5")
elif dig == 0:
    print(f"Last digit of {number} is {dig} and is 0")
else:
    print(f"Last digit of {number} is {dig} and is less than 6 and not 0")
