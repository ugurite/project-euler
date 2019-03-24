# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

import sys

def fibo_even_sequence(n):
    """Retruns fibonacci values that are even and lesser than n.
    Based on formula: E(n) = 4*E(n-1) + E(n-2)"""
    if n==0:
        return [0]
    elif n==2: 
        return [0,2]
    else:
        L = [0,2]
        while L[-1] <= n:
            L.append(4*L[-1]+L[-2])
        return L[:-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    L = fibo_even_sequence(n)
    print(sum(L))