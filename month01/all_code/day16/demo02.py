"""
    包中__init__模块的作用
        在包第一次被导入时执行,
        对外提供必要的功能

"""
import package01.package02 as p

import package01
# print(p.大爷)
p.module01.func01()
p.func01()

package01.func01()