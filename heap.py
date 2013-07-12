#!/usr/bin/env python3

class Heap:
    '''
    Max heap
    '''
    def __init__(self, buf):
        self.buffer = ['guard']
        self.buffer.extend(buf)
        self.build()

    def __str__(self):
        return str(self.buffer[1:])

    def __len__(self):
        return len(self.buffer) - 1

    def build(self):
        buf = self.buffer
        start = (len(buf) - 1) // 2
        if (len(buf) - 1) % 2 == 0:
            if buf[start] < buf[2 * start]:
                buf[start], buf[2 * start] = buf[2 * start], buf[start]
            start -= 1

        for i in range(start, 0, -1):
            self.adjust(i)

    def adjust(self, pos):
        buf = self.buffer
        end = len(self) // 2 if len(self) % 2 == 1 else len(self) // 2 - 1
        while pos <= end:
            target = pos * 2 if buf[pos * 2] > buf[pos * 2 + 1] else pos * 2 + 1
            if buf[pos] < buf[target]:
                buf[pos], buf[target] = buf[target], buf[pos]
                pos = target
            else:
                break
        if len(self) % 2 == 0 and pos == len(self) // 2:
            if buf[pos] < buf[pos * 2]:
                buf[pos], buf[pos * 2] = buf[pos * 2], buf[pos]

    def insert(self, x):
        buf = self.buffer
        buf.append(x)
        top = (len(buf) - 1) // 2
        backup = buf[top]
        if (len(buf) - 1) % 2 == 0:
            if buf[top] < buf[2 * top]:
                buf[top], buf[2 * top] = buf[2 * top], buf[top]

            if backup == buf[top]:
                return

            top //= 2

        while top >= 1:
            backup = buf[top]
            if buf[top] < buf[2 * top]:
                buf[top], buf[2 * top] = buf[2 * top], buf[top]
            if buf[top] < buf[2 * top + 1]:
                buf[top], buf[2 * top + 1] = buf[2 * top + 1], buf[top]

            if backup == buf[top]:
                return

            top //= 2

if __name__ == '__main__':
    target = [8, 7, 1, 5, 6, 2, 4, 10, 3, 9]
    h = Heap(target)
    print('Original heap: %s' % h)
    h.insert(11)
    print('After inserting 11: %s' % h)
