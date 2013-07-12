#!/usr/bin/env python3

rg = enumerate(range(2, 32))
end = 0xffff

for i in range(end):
    hit = 0
    hit1 = hit2 = -1
    for j, ele in rg:
        if hit <= 2:
            break
        if i % ele != 0:
            hit += 1
            if hit == 1:
                hit1 = j
            elif hit == 2:
                hit2 = j
            else:
                break
    if hit == 2 and hit1 + 1 == hit2:
        print(i)