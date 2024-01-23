"""
    lambda应用
        作为函数的实参

        删除在部门编号9002的所有员工
        删除在薪资大于20000的所有员工

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

# def condition01(item):
#     return item.money < 20000
#
# def condition02(item):
#     return item.did == 9002

# print(IterableHelper.delete_all(list_employees,condition01))
print(IterableHelper.delete_all( list_employees, lambda item:item.money < 20000))
print(IterableHelper.delete_all(list_employees,lambda item:item.eid == 9002))

list01 = [43, 54, 9,65, 76, 8, 9]

for item in IterableHelper.find_all(list01,lambda num:num % 2):
    print(item)
print(list(IterableHelper.find_all(list01,lambda num:num % 2)))
print(tuple(IterableHelper.find_all(list01,lambda num:num % 2)))
print(set(IterableHelper.find_all(list01,lambda num:num % 2)))








