#!/usr/bin/env python3

def binsearch(array, t):
    l, r = 0, len(array) - 1

    while l <= r:
        m = (l + r) // 2
        if array[m] < t:
            l = m + 1
        elif array[m] > t:
            r = m - 1
        else:
            return m
    return -1


if __name__ == '__main__':
    print(binsearch(list(range(10)), 5))