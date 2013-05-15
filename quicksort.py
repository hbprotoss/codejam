#!/usr/bin/env python3

import random
def quickSort(l, left, right):
    if left >= right:
        return

    x = l[left]
    i = left
    j = right
    while(i < j):
        while(i < j and l[j] > x):
            j -= 1
        if i < j:
            l[i] = l[j]
            i += 1
        while(i < j and l[i] < x):
            i += 1
        if i < j:
            l[j] = l[i]
            j -= 1
    l[i] = x
    quickSort(l, left, i-1)
    quickSort(l, i+1, right)

src = [random.randrange(0, 100) for i in range(10)]
print(src)
quickSort(src, 0, len(src)-1)
print(src)
