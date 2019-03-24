# -*- coding: utf-8 -*-
"""
@author: ugurite
"""

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = n*(n+1)//2
    sum_squares = a * (2*n+1) // 3
    squares_sum = (a)**2
    print(squares_sum-sum_squares)