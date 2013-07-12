#!/usr/bin/env python3

'''
字符串编辑距离
'''

import sys

try:
    s1, s2 = sys.argv[1:]
except ValueError:
    s1 = 'abcdef'
    s2 = 'abdgf'

table = [[0]*(len(s1)+1) for i in range(len(s2)+1)]
for i in range(len(s1)+1):
    table[0][i] = i
for i in range(len(s2)+1):
    table[i][0] = i

for i in range(1, len(s2)+1):
    for j in range(1, len(s1)+1):
        table[i][j] = min(table[i-1][j]+1, table[i][j-1]+1, table[i-1][j-1]+(0 if s1[j-1] == s2[i-1] else 1))

print(table)
print(table[-1][-1])