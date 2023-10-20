# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 19:26:33 2023

@author: Administrator
"""

import numpy as np
import random 

#初始化矩阵
row,col=5,10
M1=np.zeros((row,col),dtype=int)
M2=np.zeros((col,row),dtype=int)
#M=np.zeros((row,row),dtype=int)
##我从以下链接获得了灵感：https://deepinout.com/python/python-qa/t_how-to-create-a-matrix-of-random-integers-in-python.html
#生成随机数并填充矩阵
for i in range(row):
    for j in range(col):
        M1[i][j]=random.randint(0,50)
print(M1)
for i in range(col):
    for j in range(row):
        M2[i][j]=random.randint(0,50)       
print(M2)

#我从以下链接获得了灵感：https://www.python51.com/jc/131113.html

def Matrix_multip(M1,M2):
    m=len(M1)
    n=len(M2[0])
    result = [[0] * n for _ in range(m)]
    for i in  range(m):
        for j in  range(n):
            for k in range(len(M2)):
                result[i][j]+=M1[i][k]*M2[k][j]
    return result
"""
##测试调用函数案例
matrix1 = [[1, 2], [3, 4]] 
matrix2 = [[5, 6], [7, 8]] 
Matrix_multip(matrix1,matrix2)
"""
#调用函数
Matrix_multip(M1,M2)