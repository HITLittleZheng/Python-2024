"""
    yield -> 生成器函数
"""
"""
class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        number = 0
        while number < self.__stop:
            yield number
            number += 1
"""
def my_range(stop):
    number = 0
    while number < stop:
        yield number
        number += 1

# 循环一次,计算一次,返回一次
# for number in MyRange(5):
#     print(number)# 0 1 2 3 4
obj = my_range(5) # 返回生成器对象
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

"""
class generator: # 生成器 = 可迭代对象+迭代器
    def __iter__(self): # 可迭代对象
        return self
    
    def __next__(self): # 迭代器
        计算数据
        return 数据 
"""