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
