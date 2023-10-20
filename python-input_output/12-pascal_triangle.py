#!/usr/bin/python3
""" Pascal Triangle"""


def pascal_triangle(n):
    final = []
    if n <= 0:
        return final
    for i in range(1, n + 1):
        new_list = []
        if i < 3:
            for _ in range(i):
                new_list.append(1)
            final.append(new_list)
        else:
            new_list.append(1)
            for j in range(len(final[i - 2])):
                if (j + 1 < len(final[i - 2])):
                    new_list.append(final[i - 2][j] + final[i - 2][j + 1])
            new_list.append(1)
            final.append(new_list)
    return final
