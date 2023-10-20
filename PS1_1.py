# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 18:43:28 2023

@author: Administrator
"""
#定义函数
def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(a,b,c)
        else:
            if a>c:
                print(a,c,b)
            else:
                print(c,a,b)     
    else:
        if b<c:
            print(c,b,a)

#引用函数
#引用函数
Print_values(1,2,3)
Print_values(3,6,9)

