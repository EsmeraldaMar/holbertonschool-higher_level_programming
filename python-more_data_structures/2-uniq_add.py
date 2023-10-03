#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = []
    result = 0
    for dig in my_list:
        if dig not in uniq_int:
            uniq_int.append(dig)
    for dig in uniq_int:
        result += dig
    return (result)
