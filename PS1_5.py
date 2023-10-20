# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:19:53 2023

@author: Administrator
"""
"""

引用冯汇然同学和助教的思路，生成8个符号（遍历加、减、空白），放在1和2、2和3……8和9之间，得到所有可能的算式，再用eval( )给算式求结果
"""
####################5.1
from itertools import product

def find_expression(value):
    valid_expressions = []

    # 生成所有可能的+-组合
    for operators in product('+- ', repeat=7):
        # 循环所有组合并计算表达式
        for begin in ['1','1+','1-']:
            expression = begin
            num_str = '2'
            for op, num in zip(operators, range(3, 10)):
                if op == ' ':
                    num_str += str(num)
                else:
                    expression += num_str
                    expression += op
                    num_str = str(num)
            expression += num_str
            
            #计算表达式
            result = eval(expression)
            # 检查结果是否匹配目标
            if result == value:
                valid_expressions.append(expression)
    
    for valid_expression in valid_expressions:
        print(valid_expression + '=' + str(value))

# 调用函数
find_expression(50)
##########################5.2
def count_expression(target):
    count = 0
    valid_expressions = []
    ## 生成所有可能的+-组合
    for operators in product('+- ', repeat=7):
        
        # 循环所有组合并计算表达式
        for begin in ['1','1+','1-']:
            expression = begin
            num_str = '2'
            for op, num in zip(operators, range(3, 11)):
                if op == ' ':
                    num_str += str(num)
                else:
                    expression += num_str
                    expression += op
                    num_str = str(num)
            expression += num_str
            # 计算表达式
            result = eval(expression)
            # 检查结果是否匹配目标
            if result == target:
                valid_expressions.append(expression)
                count += 1
    return count
#调用函数
count_expression(50)


Total_solutions = []
Total_numubers = []

for i in range(1,101):
    count = count_expression(i)
    Total_solutions.append(count)
    Total_numubers.append(str(i)+'-'+str(count))

print(Total_solutions,'\n')
print(Total_numubers)

sol_max = max(Total_solutions)
num_max = Total_solutions.index(sol_max)+1
print('Number',num_max,'yields the maximum of Total_solutions: ',sol_max)

sol_min = min(Total_solutions)
num_min = Total_solutions.index(sol_min)+1
print('Number',num_min,'yields the minimum of Total_solutions: ',sol_min)


import matplotlib.pyplot as plt

#选取数据，画图
x = range(1,101)
y = Total_solutions

fig, ax = plt.subplots(figsize=(6,2))

ax.plot(x, y, linewidth=1.5)
ax.set_xlabel('The target numbers')
ax.set_ylabel('The total solutions')

plt.show()