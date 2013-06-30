#!/usr/bin/env python3

import random

def kBig(array, k):
    if k <= 0:
        return []
    if len(array) <= k:
        return array
    left, right = partition(array)
    # print(left, right)
    return kBig(left, k) + kBig(right, k - len(left))

def partition(array):
    left = []
    right = []

    rand_pos = random.randrange(1, len(array))
    array[rand_pos], array[0] = array[0], array[rand_pos]

    p = array[0]
    for el in array[1:]:
        if el < p:
            left.append(el)
        else:
            right.append(el)

    if len(left) < len(right):
        left.append(p)
    else:
        right.append(p)

    return (left, right)

if __name__ == '__main__':
    k = 10
    print(kBig(list(range(20)), k))