#!/usr/bin/env python3

def fibonacci(n):
    n0 = 0
    n1 = 1

    if n < 0:
        print("podaj n>=0")
    elif n == 0:
        return n0
    elif n == 1:
        return n1
    else:
        for i in range(1, n):
            nth = n0 + n1
            n0 = n1
            n1 = nth
        return nth


for i in range(10):
    print(fibonacci(i))
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(73) == 806515533049393
