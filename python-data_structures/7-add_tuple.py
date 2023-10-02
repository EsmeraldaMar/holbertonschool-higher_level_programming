#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < len(tuple_b):
        tuple_a, tuple_b = tuple_b, tuple_a
    res = []
    for i in range(0, len(tuple_a)):
        if (i < len(tuple_b)):
            res.append(tuple_a[i] + tuple_b[i])
        else:
            res.append(tuple_a[i])
    res = tuple(res)
    return (res)
