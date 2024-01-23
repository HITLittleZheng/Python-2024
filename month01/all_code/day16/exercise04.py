"""

"""


class MyRangeIterator:
    def __init__(self, end):
        self.__number = -1
        self.__end = end

    def __next__(self):
        if self.__number == self.__end - 1:
            raise StopIteration()
        self.__number += 1
        return self.__number


class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        return MyRangeIterator(self.__stop)

# 循环一次,计算一次,返回一次
# for number in MyRange(5):
#     print(number)# 0 1 2 3 4
obj = MyRange(100000)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
