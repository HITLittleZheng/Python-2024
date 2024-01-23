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
