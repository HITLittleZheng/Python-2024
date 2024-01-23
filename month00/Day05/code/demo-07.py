"""
    格式化字符串
        格式： "格式化占位符" %(参数值, ...)

    占位符：
        %s: 字符串格式占位符 (传递任何类型均可)
        %d: 整型占位符
        %f: 浮点型占位符   %.nf  表示小数点保留n为小数
        %%: %
"""
name = input("请输入姓名：")
age = int(input("请输入年龄："))
score = float(input("请输入成绩："))

# print("姓名为：%s, 年龄为: %d, 成绩为：%f, 排名：10%%" %(name, age, score))
# print("姓名为：%s, 年龄为: %d, 成绩为：%.2f, 排名：10%%" %(name, age, score))
# print("姓名为：%s, 年龄为: %s, 成绩为：%s, 排名：10%%" %(name, age, score))

# ''.format()
# '{} {}'.format(变量名1, 变量名2)
print("姓名为：{}, 年龄为:{} , 成绩为：{}".format(name, age, score))

# ''.format() 简写
# f'{变量名1} {变量名2}'
print(f"姓名为：{name}, 年龄为:{age} , 成绩为：{score}")

