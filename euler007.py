# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

def next_prime(l):
    m = l[-1]
    j = m+1
    while True:
        flag = True
        for item in l:
            if j%item == 0:
                flag = False
                break
        if flag:
            l.append(j)
            return l   #next_prime(l)
        j += 1
    #return l

def find_prime_numbers(n):
    l = [2]
    for i in range(1,n):
        l = next_prime(l)
    return l

t = int(input().strip())
numbers = []
for a0 in range(t):
    n = int(input().strip())
    numbers.append(n)

N = max(numbers)
L = find_prime_numbers(N)
for e in numbers:
    print(L[e-1])