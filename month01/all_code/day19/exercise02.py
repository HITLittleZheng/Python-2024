"""
    修改为标准装饰器
        -- 返回值
        -- 参数
        -- @装饰器
"""


def verify_permissions(func):
    def wrapper(*args):
        print("验证权限")
        res = func(*args)  # 调用旧功能
        return res

    return wrapper

@verify_permissions
def insert(data):
    print("插入")

@verify_permissions
def delete():
    print("删除")
    return "ok"

insert("新数据")  # 调用内函数
print(delete())
