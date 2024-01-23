"""
    变量示例
        关联一个对象的标识符。
        创建一个自定义的名, 名通过=绑定了一个值(表达式),
        方便后续的使用
"""

name = "张百万"
print(name)

# 查看python内置关键字
# import keyword
#
# print(keyword.kwlist)

age = 18
print(age)

myname = "严航"
print(myname)
# 多个英文单词之间可以这样做：
# 1. 单词之间使用 下划线_ 进行分割
my_name = "严航"
print(my_name)

# 2. 大驼峰: 每个单词首字母大小，例如：MyName
MyName = "老杨"
print(MyName)

# 3. 小驼峰：第二个(含)以后的单词首字母大写 例如：myName
myName = "老祁"
print(myName)

# 变量名1 = 变量名2 = 变量名3 = 值1
name1 = name2 = name3 = "严航"
print(name1)
print(name2)
print(name3)


# 变量修改：
info = "人工智能大家庭"
print(info)

info = "AIDTN2110人工智能大家庭"
print(info)


# 删除变量： 删除之后 会释放内存
#       再次访问时 会触发异常 NameError: xxx
del info
del name, age
print(info)