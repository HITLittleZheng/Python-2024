"""
    将高阶函数定义在公共模块中
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


def condition01(emp):
    return emp.eid == 1003


def condition02(emp):
    return emp.name == "孙悟空"


for item in IterableHelper.find_all(list_employees, condition01):
    print(item.__dict__)

result = IterableHelper.find_single(list_employees, condition02)
print(result.__dict__)
