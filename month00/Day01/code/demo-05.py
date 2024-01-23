"""
    基本输入函数
        input("提示信息")
    特点：
        1. 当程序执行到input, 等待用户输入, 输入完成之后
            才会继续向下执行
        2. 在Python中, input接收用户输入后，一般存储到变量,方便使用
        3. 在Python中, input接收用户输入的数据都当做字符串使用。
"""
print("input之前...")
name = input("请输入你的姓名：")
print("input之后...")
print(name)

# 扩展：
# type() --> 查看对象的类型
print(type(name))