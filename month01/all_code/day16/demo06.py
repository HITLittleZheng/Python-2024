"""
    人为创造异常
        快速传递错误消息的机制
        raise 异常类型(数据)       try..except
            发送                     接收
"""

class Wife:
    def __init__(self, name="", age=0):# 2
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value): # 3
        if 20 <= value <= 30:
            self.__age = value
        else:
            # 发送错误消息
            raise Exception("我不要",1001)

while True:
    # 接收错误消息
    try:
        age = int(input("请输入年龄:"))
        shuang_er = Wife("双儿", age)# 1
        break
    except Exception as e:
        print(e.args) # 读取消息

print("后续逻辑")