"""
    逻辑运算符
        and   or   not
        表达式1 and 表达式2
        表达式1 or 表达式2
        not 表达式
"""

# and 逻辑符： 一假即假
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

a = 10
b = 11
print(a > b and a < b)  # False
print(a < b and a != b)  # True

# or 逻辑符: 一真即真
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False

print(a > b or a < b)  # True
print(a < b or a != b)  # True

# not: 取反
print(not True)  # False
print(not False)  # True

# 短路运算
# 一旦结果确定，后面表达式将不再执行
# 扩展： 逻辑运算时, 尽量将复杂的(耗时的)判断放在后面
# False and ?
print(1 > 1 and input("请输入：") == "a")

# True or ?
print(3 > 1 or input("请输入") == "a")
