#!/usr/bin/env python3

L1 = [1, 2, 3, 4, 5, 5, -12]
L2 = [4, -12, 5, 6, 7, -1, 8, 9, 14]
intersection = []
union = []

for x in L1:
    if x in L2 and x not in intersection:
        intersection.append(x)
print(intersection)

for x in L1:
    if x not in union:
        union.append(x)
for x in L2:
    if x not in union:
        union.append(x)
print(union)
