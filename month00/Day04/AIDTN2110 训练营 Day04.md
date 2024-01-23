# AIDTN2110 训练营 Day04

<https://www.processon.com/view/link/61721b095653bb7318cc5bb7>

```python
"""
    模拟出租车计价器
        1. 起步价: 13元包含3公里.
        2. 超过3公里, 但是没有超过15公里: 每公里2.3元.
        3. 如果超过15公里: 每公里加收2.3元的50%.
        要求：计算的最终费用 保留两位小数.

    完成之后, 复习今天知识, 操作 debug 调试模式[多操作几遍]。
"""
# 1. 获取数据
# km = float(input("请输入一个公里数："))
# price = 13

# 2. 逻辑计算
# if 0 < km <= 3:
#     price = price
#
# elif 3 < km <= 15:
#     # price = (km - 3) * 2.3 + price
#     price += (km - 3) * 2.3
#
# elif km > 15:
#     # price = price + 12 * 2.3 + (km - 15) * 2.3 * 1.5
#     price += 12 * 2.3 + (km - 15) * 2.3 * 1.5
#
#
# # 3. 打印输出
# print("费用", round(price, 2))

# 代码优化：
km = float(input("请输入一个公里数："))
price = 13

if km > 0:
    if 0 < km <= 3:
        price = price

    elif 3 < km <= 15:
        # price = (km - 3) * 2.3 + price
        price += (km - 3) * 2.3

    elif km > 15:
        # price = price + 12 * 2.3 + (km - 15) * 2.3 * 1.5
        price += 12 * 2.3 + (km - 15) * 2.3 * 1.5

    print("费用", round(price, 2))

else:
    print("公里数有误！")


```

## while 循环

- 作用：根据一定条件重复胡执行一条或多条语句。

- 语法：

  ```python
  while 条件表达式:
      满足条件表达式执行的代码块
  else:
      不满足条件表达式执行的代码块
  ```

- 说明：else 子句可以0个或1个。

```python
"""
    跑圈
    while 循环语法：
        while 条件表达式:
            满足条件表达式执行的语句

"""

# print("跑圈")
# print("跑圈")
# print("跑圈")
# print("跑圈")
# print("跑圈")

# 计数器
# count = 0
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print(count)


# while 语句
count = 0
while count < 5:
    print("跑圈")
    count += 1
else:
    print("跑完了", count)

```

```python
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
```

```python
"""
    循环录入五个成绩, 最后打印平均成绩
"""

count = 0
total_score = 0
while count < 5:
    score = float(input("请输入成绩："))
    count += 1

    total_score += score

print('平均成绩为：', total_score / 5)

```

```python
"""
    输入两个数, 分别代表起始值 和 终止值.
    根据 输入值大小,可以升序 或 降价打印输入。
    起始值： 1
    终止值: 10
    打印为: 1 2 3 4 5 6 7 8 9 10

    打印为: 10 9 8 7 6 5 4 3 2 1
"""
start = int(input("请输入起始值:"))
end = int(input("请输入终止值:"))

# while start <= end:
#     print(start, end=" ")
#     start += 1


while start <= end:
    print(end, end=" ")
    end -= 1

```

```python
"""
    将 1 - 20 之间的整数, 每五个数是一行进行打印
"""

i = 0
while i < 20:
    i += 1
    print(i, end=" ")
    if i % 5 == 0:
        print()

```

## 死循环

```python
"""
    死循环：
        一个无法依靠自身的控制终止的循环
        条件表达式一直成立

        while 条件表达式:
            循环体
        else:
            不满足条件执行的语句
            
        break 语句： 用来终止当前循环执行的语句
"""
num = 1

# 条件一直成立[便于记忆]
# while num < 10:
#     print(num)


# while 1:
#     pass


# 推荐写法
while True:
    score = input("请输入学员成绩（输入'exit'表示退出）")

    # if not score:
    #     break  # 终止循环

    if score == "exit":
        break

```

## break 语句

```python
"""
    break 语句
        用来终止当前循环语句
    说明：
        1. 当break 语句之后后, 此循环中break之后的语句将不再执行;
        2. 当break 终止循环时, 循环语句的else子句将不再执行;
        3. 如果有循环嵌套时, break语句只终止本次循环, 执行外层循环;
        4. break 语句只能在循环语句(while for)中使用
"""

i = 1
while True:
    print(i)
    break  # 终止当前循环


# 1. 当break语句执行后, 此循环语句中 break 之后的语句将不再执行
while True:
    name = input("请输入姓名：")
    # 当输入为空时 终止循环
    # if not name:
    if name == "":
        break
        print('执行了break')


# 2. break 语句终止循环时, 循环语句的else子句将不会执行
while True:
    name = input("请输入姓名：")
    # 当输入为空时 终止循环
    # if not name:
    if name == "":
        break
else:
    print('执行了break')


# 3. break 语句只能终止当前循环, 如果有循环嵌套时, 跳出本次循环，执行外层循环
while True:
    print("外层循环开始！")
    name = input("输入姓名：")

    while True:
        print("内层循环开始！")
        score = input("请输入成绩'exit'表示退出")
        if score == 'exit':
            break

    print("退出了内层循环, 进入外层循环！！")
    break

```

```python
"""
    循环猜数：
        直到猜对为止，打印共猜测次数
"""
import random

random_number = random.randint(1, 100)

count = 0
while True:
    # 循环的让用户去猜测
    print(random_number)
    user_number = int(input("请输入您猜测的数："))
    count += 1

    if user_number > random_number:
        print("猜大了")
    elif user_number < random_number:
        print("猜小了")
    else:
        print("恭喜您, 终于猜对了, 您一共猜了", count, "次")
        break

```

## continue 语句

```python
"""
    continue 语句:
        跳过本次循环，直接继续下一次循环
    说明：
        1. continue语句执行后,将不再执行本次循环内continue之后的语句
        2. continue语句 适用于循环语句(for/while)
            while 循环中, 执行continue 将会直接从continue跳转到条件表达处

    需求：
        输入两个数, 分别代表起始值 和 终止值.
        根据 输入值大小,可以升序 或 降价打印输入。
        遇到 4 跳过 不输出
"""

start = int(input("请输入起始值:"))
end = int(input("请输入终止值:"))

while start <= end:
    start += 1
    if start == 4:
        continue  # 跳过本次循环

    print(start, end=" ")


```

```python
"""
    打印 10-20 的数字  个位 非 3 5 7 的数.
"""

num = 9
while num <= 20:
    num += 1
    ge_number = num % 10

    if ge_number == 3 or ge_number == 5 or ge_number == 7:
        continue

    print(num)

```

```python
break  vs continue 

# 相同点：
1. break、continue  均需使用在循环语句(for while)中
2. break、continue  语句之后的语句不再执行

# 不同点:
1. break: 直接终止循环
2. continue: 跳过本次循环,继续下一次循环

```

## for 循环

- 语法：

  ```python
  for 变量 in 可迭代对象:
      代码块1
  else:
      代码块2
  ```

- 可迭代对象：能够依次获取数据的对象。包含：非空字符串，非空列表...

```python
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
            2. 可迭代对象不能数据元素后,执行else子句部分,然后退出循环;
            3. else 子句可以省略
"""

info = "Python"

# item: 项
for item in info:
    print(item)
else:
    print("else 子句")
```

```python
"""
    用户输入一个字符串, 将该字符串中的字符逐一打印.
"""

user_info = input("请输入：")

for item in user_info:
    print(item)


```

## range() 函数

- 功能：用来生成一系列的整数可迭代对象。

- 格式：

  ```python
  range([start], stop, [step]) # [] --> 可选
  
  start:起始值, 默认为0, 可以省略
  stop:终止值， 必须存在， 终止值无法获取
  step:步长， 默认为1，可正可负，可以省略    
  ```

- 返回：一个整数的range对象

- 说明：从 start 开始，每次生一个整数移动step，直到stop结束。

```python
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

```

```python
"""
    循环 打印 1-10之间的奇数

    计算20以内不能被2 5 整数的数之和
"""

# num = 0
# while num < 10:
#     num += 1
#     if num % 2 == 0:
#         continue
#     print(num)

# for item in range(1, 11):
#     if item % 2:
#         print(item)

# for item in range(1, 11, 2):
#     print(item)


sums = 0
for i in range(20):
    if not i % 2 or not i % 5:
        continue
    # print(i)
    sums += i

print('最终的和为：', sums)

```

```python
"""
    注意
"""

# 1. 起始值和终止值相同, 则结果为空
for item in range(1, 1, 2):
    print(item)

# 2. 取值反向与步长方向不一致, 则结果为空
for item in range(5, 1):
    print(item)
```

```python
# 循环小结：
for 循环：
	场景：用于已知循环次数(写法简单)

while 循环:
    场景：用于位置循环次数

```

```python
"""
    循环录入五个成绩, 最后打印平均成绩
"""

total_score = 0

for i in range(5):
    score = float(input("请输入成绩: "))
    total_score += score

print("平均成绩为：", total_score / 5)

```



















