#! /usr/bin/env python3

# 3.4
while True:
    line = input()
    if line == "stop":
        break
    else:
        try:
            number = float(line)
        except ValueError:
            print("Nie wprowadzono liczby!")
        else:
            print(f"{number**3},{number}")
