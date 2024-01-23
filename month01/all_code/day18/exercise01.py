"""
    day17/exercise07.py
    使用IterableHelper+lambda实现以下功能:
        -- 查找编号是1005的单个员工
        -- 查找部门是9001的所有员工
        -- 查找姓名是2个字的所有员工
        -- 查找薪资小于3w的第一个员工
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

# def condition01(p):
#     return p.eid == 1005

# emp01 = IterableHelper.find_single(list_employees, condition01)
emp01 = IterableHelper.find_single(list_employees, lambda p: p.eid == 1005)
print(emp01.__dict__)

for item in IterableHelper.find_all(list_employees, lambda emp: emp.did == 9001):
    print(item.__dict__)

for item in IterableHelper.find_all(list_employees, lambda emp: len(emp.name) == 2):
    print(item.__dict__)

emp = IterableHelper.find_single(list_employees, lambda e: e.money < 30000)
print(emp.__dict__)
