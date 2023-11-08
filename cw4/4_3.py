#!/usr/bin/env python3

import math


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


for i in range(10):
    print(f"{i}! = {factorial(i)}")
assert factorial(0) == math.factorial(0)
assert factorial(14) == math.factorial(14)
