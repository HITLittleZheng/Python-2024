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
