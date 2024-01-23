"""
    迭代 iteration
        每次都会在之前基础上有所增加的重复过程
    迭代器 iter ator
        完成迭代过程的对象
    可迭代对象 iter able
        创建迭代器的对象
"""
message = "我是齐天大圣孙悟空"
# 遍历
for item in message:
    print(item)
# 学习for循环原理(内部代码)
# 1. 获取迭代器
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
        # 3. 如果停止迭代则退出循环
    except StopIteration:
        break
# 面试题:
# 能够参与for循环的条件是什么?
# 答:对象具有__iter__函数
#    能够获取迭代器对象(是可迭代对象)
#