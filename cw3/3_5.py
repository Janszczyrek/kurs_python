#! /usr/bin/env python3

import math

# 3.5
miarka = '|'
try:
    length = int(input('Podaj długość miarki: '))
    tab_count = 4 if length < 1000 else int(math.log(length, 10))+1
    for i in range(length):
        miarka += '.' * tab_count + '|'
    miarka += '\n'
    for i in range(length + 1):
        if i in [10**x for x in range(1, len(str(length)))]:
            tab_count -= 1
        miarka += str(i) + ' ' * tab_count
    print(miarka)
except ValueError:
    print("Nie wprowadzono liczby!")
