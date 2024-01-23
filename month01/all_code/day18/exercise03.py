"""
    需求：
        定义函数，获取员工列表中部门编号是9001的员工数量
        定义函数，获取员工列表中姓名是3个字的员工数量
    步骤：
    ​    -- 根据需求，写出函数。
    ​    -- 因为主体逻辑相同,核心算法不同.
    ​       所以使用函数式编程思想直接创建通用函数get_count
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
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

"""
def get_count01():
    count = 0
    for item in list_employees:
        if item.did == 9001:
            count += 1
    return count


def get_count02():
    count = 0
    for item in list_employees:
        if len(item.name) == 3:
            count += 1
    return count


def get_count(condition):
    count = 0
    for item in list_employees:
        # if item.did == 9001:
        # 先确定用法
        if condition(item):
            count += 1
    return count

# 后实现功能
get_count(lambda item: item.did == 9001)
"""

print(IterableHelper.get_count(list_employees, lambda e: e.did == 9001))

IterableHelper.select(list_employees,lambda e:(e.eid,e.money))

