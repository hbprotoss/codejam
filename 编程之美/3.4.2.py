#!/usr/bin/env python3

'''
只遍历一次来反转链表
'''

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        rtn = []
        cur = self
        while cur:
            rtn.append(str(cur.data))
            cur = cur.next
        return ' -> '.join(rtn)

def reverse(head):
    pre, cur, next = None, head, head.next
    while cur:
        next = cur.next
        cur.next = pre
        pre, cur = cur, next
    return pre

length = 10
l = [Node(i, None) for i in range(length)]
for i in range(length-1):
    l[i].next = l[i + 1]
l[length-1].next = None

head = l[0]
print(head)
print(reverse(head))