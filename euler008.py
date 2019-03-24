# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

def f(num, n, k):
    l = []
    for i in range(n-k):
        digits = num[i:i+k]
        m = 1
        for e in digits:
            m = m*int(e)
        l.append(m)
    return max(l)

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(f(num, n, k))