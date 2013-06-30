#!/usr/bin/env python3
# coding=utf-8

import re
from fractions import gcd

# Pattern for '0.123(456)'
pattern = r'(\d*)\.(\d*)\((\d*)\)'


def reduce(func):
    def reduce_wrapper(*arg, **kwarg):
        a, b = func(*arg, **kwarg)
        if a > b:
            a, b = b, a
        _gcd = gcd(b, a)
        return (a // _gcd, b // _gcd)
    return reduce_wrapper

@reduce
def circleToFraction(circle):
    '''
    Convert circle part to fraction
    @params circle: string.
    '''
    numerator = int(circle)                 # 分子
    denominator = 10 ** len(circle) - 1     # 分母
    return (numerator, denominator)

@reduce
def decimalToFraction(non_circle):
    return (int(non_circle), 10 ** len(non_circle))

@reduce
def add(fraction1, fraction2):
    return (fraction1[0]*fraction2[1] + fraction1[1]*fraction2[0], fraction1[1]*fraction2[1])

if __name__ == '__main__':
    src = input('Input decimal fraction(in the form of "0.123(456)"):')
    integer, non_circle, circle = re.findall(pattern, src)[0]
    print(integer, non_circle, circle)

    a_numerator, a_denominator = circleToFraction(circle)
    a_denominator *= (10 ** len(non_circle))
    print(a_numerator, a_denominator)

    if non_circle:
        b_numerator, b_denominator = decimalToFraction(non_circle)
        print(b_numerator, b_denominator)

        numerator, denominator = add((a_numerator, a_denominator), (b_numerator, b_denominator))
    else:
        numerator, denominator = a_numerator, a_denominator
    print('%d / %d' % (numerator, denominator))