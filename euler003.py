# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

import math

def decompose(n):
    if n==2:
        return {n}
    elif n%2==0:
        return {2}.union(decompose(n//2))
    else :
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i==0:
                return decompose(i).union(decompose(n//i))
    return {n}

def largest_prime(n):
    l = sorted(list(decompose(n)))
    return l[-1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(largest_prime(n))

