"""
    容器常用函数(自学)
        记住:容器对应的操作(中文)
"""
message = "我是:齐天大圣"
print(message.startswith("大圣")) # False
print(message.startswith("我"))# True
print(message.startswith("我是"))# True
print(message.startswith("齐天",3))# False