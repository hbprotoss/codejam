#!/usr/bin/env python3

from copy import deepcopy
import sys

A = [
    [1, 1],
    [1, 0]
]

def matrixMultiply(A, B):
    '''
    A = A * B
    '''
    for i in range(len(A)):
        tmp = [0] * len(B)
        for j in range(len(B[0])):
            for k in range(len(B)):
                tmp[j] += A[i][k] * B[k][j]
        A[i] = tmp
    return A

def matrixPow(matrix, n):
    # rtn初始化成单位矩阵
    rtn = [[0]*len(matrix) for i in range(len(matrix))]
    for i in range(len(matrix)):
        rtn[i][i] = 1

    power = deepcopy(matrix)

    index = 1
    while True:
        # print('power %d:\t%s' % (index, power))
        # print('rtn:\t\t%s' % rtn)
        # index <<= 1

        if n & 1:
            matrixMultiply(rtn, power)
        n >>= 1

        # 退出条件不放在while是为了最后能少一次矩阵乘法
        if not n:
            break

        # power ** x
        power_tmp = deepcopy(power)
        matrixMultiply(power, power_tmp)
    return rtn

if __name__ == '__main__':
    rtn = matrixPow(A, int(sys.argv[1]))
    print(rtn)