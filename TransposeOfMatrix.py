# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 11:02:54 2019

@author: rajak
"""

a=[[1,2,3],
   [4,5,6],
   [7,8,9]]
b=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        b[i][j]=b[i][j]+a[j][i]
print(b)