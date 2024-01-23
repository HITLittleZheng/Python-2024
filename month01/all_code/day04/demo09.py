"""
    索引
        定位单个元素
        容器名[整数]
"""
msg = "花果山齐天大圣孙悟空"
print(msg[1]) # 定位第二个元素
print(len(msg)) # 10
print(msg[len(msg)-1]) # 定位最后一个元素
print(msg[-1])
print(msg[-3])
# IndexError: string index out of range
# print(msg[100])

