# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 20:44:45 2023

@author: Administrator
"""



#定义函数
"""
我从以下链接获得了灵感:https://blog.csdn.net/qq_45208848/article/details/114642662?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-114642662-blog-113983632.235^v38^pc_relevant_anti_vip&spm=1001.2101.3001.4242.1&utm_relevant_index=3
杨辉三角形又称Pascal三角形，它的第i+1行是(a+b)i的展开式的系数。
它的一个重要性质是:三角形中的每个数亨等于它两肩上的数字相加。
"""
def Pascal_triangle():
    n=int(input())
    a=[]
    for i in range(1,n+1):
        a.append(1)
        if i>2:
            b=a[:]
            for n in range(1,len(a)-1):
                a[n]=b[n-1]+b[n]
        for k in a:
            print(k,end=' ')
        print(' \n')
    
#调用函数
Pascal_triangle()
