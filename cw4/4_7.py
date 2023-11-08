#!/usr/bin/env python3


def flatten(sequence):
    def flatten_rec(sequence, result):
        for x in sequence:
            if isinstance(x, (list, tuple)):
                flatten_rec(x, result)
            else:
                result.append(x)
    result = []
    flatten_rec(sequence, result)
    return result


L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
flat = flatten(L)
print(flat)
