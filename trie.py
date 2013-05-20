#!/usr/bin/env python3

class Trie:
    root = dict()

    def insert(self, string):
        index, node = self.findLastNode(string)
        for char in string[index:]:
            new_node = dict()
            node[char] = new_node
            node = new_node

    def find(self, string):
        index, node = self.findLastNode(string)
        return (index == len(string))

    def findLastNode(self, string):
        '''
        @param string: string to be searched
        @return: (index, node).
            index: int. first char(string[index]) of string not found in Trie tree. Otherwise, the length of string
            node: dict. node doesn't have string[index].
        '''
        node = self.root
        index = 0
        while index < len(string):
            char = string[index]
            if char in node:
                node = node[char]
            else:
                break
            index += 1
        return (index, node)

    def printTree(self, node, layer):
        if len(node) == 0:
            return '\n'

        rtns = []
        items = sorted(node.items(), key=lambda x:x[0])
        rtns.append(items[0][0])
        rtns.append(self.printTree(items[0][1], layer+1))

        for item in items[1:]:
            rtns.append('.' * layer)
            rtns.append(item[0])
            rtns.append(self.printTree(item[1], layer+1))

        return ''.join(rtns)

    def __str__(self):
        return self.printTree(self.root, 0)

if __name__ == '__main__':
    tree = Trie()
    while True:
        src = input()
        if src == '':
            break
        else:
            tree.insert(src)
            pass

    print(tree)