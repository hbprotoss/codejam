#!/usr/bin/env python3

'''
Knuth-Morris-Pratt algorithm
'''

def getPrefix(pattern):
    '''
    @param pattern: pattern string.
    @return: prefix array.
    '''
    length = len(pattern)
    prefix = [0] * length
    for i in range(1, length):
        k = prefix[i-1]
        while k > 0 and pattern[i] != pattern[k]:
            k = prefix[k-1]
        if pattern[i] == pattern[k]:
            prefix[i] = k + 1

    return prefix

def KMP(src, pattern):
    prefix = getPrefix(pattern)
    print(prefix)
    i = j = 0
    src_len = len(src)
    pattern_len = len(pattern)

    if src_len < pattern_len:
        return -1

    while i < src_len:
        while src[i] == pattern[j]:
            if j == pattern_len - 1:
                return i - j
            else:
                i += 1
                j += 1
        if j > 0:
            j = prefix[j-1]
        else:
            i += 1
    return -1

src = 'bbc abcdab abcdabcdabde'
pattern = input('pattern: ')#'abcdabd'
#print(KMP(src, pattern))
print(getPrefix(pattern))