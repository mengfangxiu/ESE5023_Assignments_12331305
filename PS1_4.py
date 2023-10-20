# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:18:00 2023

@author: Administrator
"""
"""
引用冯汇然同学和助教张鹏的思路，逆过程就是从x块钱变成1块钱，需要的次数都是一样的。从x变到1，除以2肯定比减1“更快”
所以只要x是偶数就除以2，是奇数就减1再除以2，一直循环这个过程，直到x变成1
"""
##定义函数
import random

def Least_moves(x):
    i=1
    while x!=2:
        if x%2!=0:
            x-=1
            i+=1
        else:
            x/=2
            i+=1
    print(i)
    
 
  #调用函数
Least_moves(2)  
Least_moves(5)  
a=random.randint(1,100)
print(a)
Least_moves(a) 


    