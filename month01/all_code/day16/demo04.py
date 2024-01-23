"""
    异常
        适用性:针对的是逻辑错误,而不是语法错误.
        现象:不断向上返回
"""


# 语法错误
# print(qtx) # NameError
# print("1" + 1) # TypeError
# class MyClass:
#     pass
# print(MyClass.xx) # AttributeError

# 逻辑错误:因为数据超过有效范围而已发的错误
def div_apple(apple_count):  # 3
    person_count = int(input("请输入人数:"))  # ValueError
    result = apple_count / person_count  # ZeroDivisionError
    print(f"每人{result}个苹果")

def main():  # 2
    div_apple(10)

main()  # 1

print("后续逻辑")
