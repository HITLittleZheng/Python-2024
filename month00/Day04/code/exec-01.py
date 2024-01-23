"""
    打印 1 2 3 4 ... 20 之间的整数
    说明：
        1. 创建初始变量
        2. 条件中使用变量
        3. 循环体中 向不满足条件逐步演进
"""

# 1. 创建初始变量
num = 1

# 2. 循环条件 num <= 20
while num <= 20:
    # 3. 循环事情： print(num)
    print(num, end=" ")
    num += 1

print()
"""
    20 18 16 14 ... 6 4 2 
"""

number = 20

while number >= 0:
    print(number, end=" ")
    number -= 2
else:
    print()
    print("结束")