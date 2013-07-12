#!/usr/bin/env python3

import sys

source = int(sys.argv[1])
n = 2 if source % 2 == 1 else 3

while True:
    avg = source / n
    if avg <= n // 2:
        break

    # source能整除n，或者除下结果为x.5
    remainder = source % n
    if (remainder != 0) and (n / remainder != 2):
        n += 1
        continue

    avg = int(avg)
    start = avg - n // 2 if n % 2 == 1 else avg - n // 2 + 1
    print(' + '.join((str(i) for i in range(start, start + n))))
    n += 1