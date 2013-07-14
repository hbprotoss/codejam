#!/usr/bin/env python3

'''
n个数中随机选出m个数
'''

import sys
from random import randrange

def randSelect(n, m):
    rtn = []
    for i in range(n):
        if randrange(0, 0xffff) % (n - i) < m:
            rtn.append(i)
            m -= 1

    return rtn

try:
    n, m = sys.argv[1:]
except ValueError:
    n, m = 50, 6

for i in range(50):
    res = randSelect(n, m)
    # print(res)
    assert len(res) == m
