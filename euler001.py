# -*- coding: utf-8 -*-
"""
@author: ugurite
"""


# Hacker Rank submission


def euler1(n):
    # 3
    n3 = (n-1)//3
    s3 = 3*n3*(n3+1)//2
    # 5
    n5 = (n-1)//5
    s5 = 5*n5*(n5+1)//2
    # 15
    n15 = (n-1)//15
    s15 = 15*n15*(n15+1)//2
    return int(s3 + s5 - s15)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(euler1(n))