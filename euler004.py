# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

import math

def is_palindrome(n):
    l = list(str(n))
    return l==l[::-1]

def is_3digits_product(n):
    for i in range(100, min(1000, int(math.sqrt(n))+1)):
        if n%i==0:
            j = n//i
            str_j = str(j)
            if len(str_j) < 3:
                return False
            elif len(str_j)==3:
                return True
            else: 
                pass
    return False

def find_palindrome(n):
    for i in range(n-1, 101100, -1):
        if is_palindrome(i):
            if is_3digits_product(i):
                return i
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_palindrome(n))
