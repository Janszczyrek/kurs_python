#!/usr/bin/env python3

def odwracanie_iter(L, left, right):
    try:
        while left < right:
            temp = L[left]
            L[left] = L[right]
            L[right] = temp
            left, right = left + 1, right - 1
    except IndexError:
        print("odwolanie poza zakres listy!")


def odwracanie_rec(L, left, right):
    try:
        if left >= right:
            pass
        else:
            temp = L[left]
            L[left] = L[right]
            L[right] = temp
            odwracanie_rec(L, left+1, right-1)
    except IndexError:
        print("odwolanie poza zakres listy!")


L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

odwracanie_iter(L, 3, 9)
assert L == [0,1,2,9,8,7,6,5,4,3]
odwracanie_iter(L, 0, 9)
assert L == [3,4,5,6,7,8,9,2,1,0]
odwracanie_iter(L, 0, 1)
assert L == [4,3,5,6,7,8,9,2,1,0]
odwracanie_iter(L, 8, 9)
assert L == [4,3,5,6,7,8,9,2,0,1]


odwracanie_rec(L, 5, 7)
assert L == [4,3,5,6,7,2,9,8,0,1]
odwracanie_rec(L, 3, 9)
assert L == [4,3,5,1,0,8,9,2,7,6]
odwracanie_rec(L, 0, 1)
assert L == [3,4,5,1,0,8,9,2,7,6]
odwracanie_rec(L, 8, 9)
assert L == [3,4,5,1,0,8,9,2,6,7]
print(L)
