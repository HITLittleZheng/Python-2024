"""
    for 循环：
        语法：
            for 变量 in 可迭代对象:
                代码块1
            else:
                代码块2
        作用：
            用来遍历序列或可迭代对象中的每一个元素
        说明：
            1. 变量依次用可迭代对象每次给出的元素, 然后执行代码块1;
            2. 可迭代对象不能提供数据元素后,执行else子句部分,然后退出循环;
            3. else 子句可以省略
"""

info = "Python"

# item: 项
for item in info:
    print(item)
else:
    print("else 子句")