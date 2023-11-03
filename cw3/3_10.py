#!/usr/bin/env python3

# 3.10
roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabic = [1, 5, 10, 50, 100, 500, 1000]

dict1 = dict(zip(roman, arabic))
dict2 = {roman[i]: arabic[i] for i in range(len(roman))}
dict3 = dict(map(lambda i, j: (i, j), roman, arabic))
