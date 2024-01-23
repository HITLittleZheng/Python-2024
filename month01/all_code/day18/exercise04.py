"""
    需求：
        定义函数，在员工列表中查找是否具有姓名相同的员工
        定义函数，在员工列表中查找是否具有薪资相同的员工
    步骤：
    ​    -- 根据需求，写出函数。
    ​    -- 因为主体逻辑相同,核心算法不同.
    ​       所以使用函数式编程思想直接创建通用函数is_repeat
       -- 将通用函数移动到IterableHelper中
          最后在当前模块中调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1002, 9001, "孙悟空", 120000),
    Employee(1005, 9001, "小白龙", 15000),
]
"""
def is_repeat01():
    for r in range(len(list_employees)-1):
        for c in range(r+1,len(list_employees)):
            if list_employees[r].name == list_employees[c].name:
                return True  # 有相同
    return False# 无相同

def is_repeat02():
    for r in range(len(list_employees)-1):
        for c in range(r+1,len(list_employees)):
            if list_employees[r].money == list_employees[c].money:
                return True  # 有相同
    return False# 无相同


def is_repeat(condition):
    for r in range(len(list_employees)-1):
        for c in range(r+1,len(list_employees)):
            # if list_employees[r].name == list_employees[c].name:
            if condition(list_employees[r]) == condition(list_employees[c]):
                return True  # 有相同
    return False# 无相同

print(is_repeat(lambda e:e.name))
"""

print(IterableHelper.is_repeat(list_employees, lambda e: e.money))
