"""
    内存图练习
"""


class Wife:
    def __init__(self, name="", age=22):
        self.name = name
        self.age = age


# (1)
jian_ning = Wife("建宁", 26)
shuang_er = jian_ning
shuang_er.name = "双儿"
print(jian_ning.name)  # ?

# (2)
jian_ning = Wife("建宁", 26)
list01 = [
    jian_ning,
    Wife("阿珂", 25),
    Wife("双儿"),
]
def func01():
    list01[0].name = "公主"
    list01[1] = Wife("苏苏")
    del list01[-1]
func01()
print(list01)
