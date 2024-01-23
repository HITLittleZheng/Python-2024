"""
    模块 module (文件)
"""
# "我过去"
# 语法:
# import 模块名
# 模块名.成员
# 本质:
# 创建变量存储目标文件的地址
from package01.package02 import module01

module01.func01()
module01.func02()

# "你过来"
# 语法:
# from 模块名 import 成员
# 直接使用成员
# 本质:
# 目标文件中的成员导入到当前文件作用域
# 注意:小心成员名称冲突
from package01.package02.module01 import func02, func03


def func01():
    print("demo-func01")

func01()
func02()
func03()
