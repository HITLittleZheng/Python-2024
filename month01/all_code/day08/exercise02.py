"""
    练习2：创建函数,在终端中打印矩形.
    number = int(input("请输入整数:"))  # 5
    for row in range(number):
        if row == 0 or row == number - 1:
            print("*" * number)
        else:
            print("*%s*" % (" " * (number - 2)))
"""

"""
def print_rectangular():
    number = int(input("请输入整数:"))  # 5
    for row in range(number):
        if row == 0 or row == number - 1:
            print("*" * number)
        else:
            print("*%s*" % (" " * (number - 2)))

print_rectangular()
"""


def print_rectangular(number, character):
    for row in range(number):
        if row == 0 or row == number - 1:
            print(character * number)
        else:
            print(character + " " * (number - 2) + character)

print_rectangular(5, "#")
# ..
size = int(input("请输入数字："))
print_rectangular(size, "$")
