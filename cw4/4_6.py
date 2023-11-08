#!/usr/bin/env python3
def sum_seq(sequence):
    global suma
    for x in sequence:
        if isinstance(x, (list, tuple)):
            sum_seq(x)
        else:
            suma += x


L = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
suma = 0
sum_seq(L)
assert suma == 45
print(suma)
