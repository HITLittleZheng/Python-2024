"""
    Python语言项目结构
项目根目录
    包
        模块
            类
                函数
                    语句
"""

# 绝对路径:从项目根目录开始

# "我过去"
from package01.package02 import module01 as m

m.func01()

# "你过来"
from package01.package02.module01 import func01

func01()
