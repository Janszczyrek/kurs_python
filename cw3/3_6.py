#!/usr/bin/env python3

try:
    edge_length = 3
    rows_count = int(input('Podaj ilość wierszy: '))
    cols_count = int(input('Podaj ilość kolumn: '))
    rectangle = ""
    for i in range(2 * rows_count + 1):
        for j in range(cols_count):
            if i % 2 == 0:
                rectangle += "+" + "-" * edge_length
            else:
                rectangle += "|" + " " * edge_length
        rectangle += ("+" if i % 2 == 0 else "|") + "\n"
    print(rectangle)
except ValueError:
    print("Nie wprowadzono liczby!")
