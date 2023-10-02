#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    while len(tuple_a) < 2:
        tuple_a += (0,)
    while len(tuple_b) < 2:
        tuple_b += (0,)
    res = []
    for i in range(0, 2):
        res.append(tuple_a[i] + tuple_b[i])
    res = tuple(res)
    return (res)
