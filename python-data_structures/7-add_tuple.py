#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    res = []
    for i in range(0, len(tuple_a)):
        if (i < len(tuple_b)):
            res.append(tuple_a[i] + tuple_b[i])
        else:
            res.append(tuple_a[i])
    res = tuple(res)
    return (res)
