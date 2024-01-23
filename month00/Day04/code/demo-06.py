"""
    整数生成器
        range([start], stop, [step]) # [] --> 可选
            start:起始值, 默认为0, 可以省略
            stop:终止值， 必须存在， 终止值无法获取
            step:步长， 默认为1，可正可负，可以省略
"""

# start=0, stop=10, step=1
# 表示：生成0-10的整数,不包含10
# range(10)
for item in range(10):
    print(item, type(item))

# start=5, stop=16, step=1
# 表示：生成5-16的整数,不包含16
# range(5, 16)
for item in range(5, 16):
    print(item, type(item))

# start=-5, stop=2, step=1
# 表示：生成-5--2的整数,不包含2
for item in range(-5, 2):
    print(item, type(item))


# start=1, stop=9, step=2
# 表示：生成1--9的整数
for item in range(1, 9, 2):
    print(item)

# start=9, stop=2, step=-3
# 表示：生成9--2的整数
for item in range(9, 2, -3):
    print(item)
