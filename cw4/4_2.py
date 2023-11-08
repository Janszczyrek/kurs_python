#!/usr/bin/env python3

import math


def make_ruler(length):
    try:
        miarka = '|'
        tab_count = 4 if length < 1000 else int(math.log(length, 10))+1
        for i in range(length):
            miarka += '.' * tab_count + '|'
        miarka += '\n'
        for i in range(length + 1):
            if i in [10**x for x in range(1, len(str(length)))]:
                tab_count -= 1
            miarka += str(i) + ' ' * tab_count
        return miarka
    except:
        raise Exception("bledne argumenty!")


def make_grid(rows, cols):
    try:
        edge_length = 3
        rectangle = ""
        for i in range(2 * rows + 1):
            for j in range(cols):
                if i % 2 == 0:
                    rectangle += "+" + "-" * edge_length
                else:
                    rectangle += "|" + " " * edge_length
            rectangle += ("+" if i % 2 == 0 else "|") + "\n"
        return rectangle
    except:
        raise Exception("bledne argumenty!")


print(make_ruler(10))
print(make_grid(4, 2))
