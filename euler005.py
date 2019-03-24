# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

def next_prime(l,n):
    m = l[-1]
    j = m+1
    while j<=n:
        flag = True
        for item in l:
            if j%item == 0:
                flag = False
                break
        if flag:
            l.append(j)
            return next_prime(l, n)
        j += 1
    return l

def find_prime_numbers(n):
    if n==1:
        return [1]
    else:
        return next_prime([2],n)
    
def to_largest_power(l,n):
    powers = []
    for e in l:
        if e==1:
            powers.append(1)
        else:
            for i in range(4, 0, -1):
                if e**i <=n :
                    powers.append(i)
                    break
    return powers
        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l = find_prime_numbers(n)
    powers = to_largest_power(l,n)
    m = 1
    for i in range(len(l)):
        m = m*(l[i]**powers[i])
    print(m)
