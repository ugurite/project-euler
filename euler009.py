# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

import math

def triplets(n):
    l = []
    lim_c = int(n/(1+math.sqrt(2)))
    for c in range(n//2-1,lim_c, -1):
        f1 = n-c
        sqrt_delta = math.sqrt(2*(c**2) - f1**2)
        if abs(sqrt_delta - int(sqrt_delta)) < 10**(-12):
            sqrt_delta = int(sqrt_delta)
            b = (f1+sqrt_delta)//2
            a = n-c-b
            l.append([c,b,a])
    return l

def f(l):
    le = len(l)
    if le==0:
        return -1
    else:
        prods = []
        for e in l:
            prods.append(e[0]*e[1]*e[2])
        return max(prods)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    #print(triplets(n))
    print(f(triplets(n)))