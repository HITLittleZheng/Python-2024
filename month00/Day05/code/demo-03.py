"""
    运算符
        1. 算数运算符： +  *
            + ： 用于字符串类型的拼接
            * ： 用于将字符串重复指定次数
        2. 复合赋值运算符
            += ： 表示将拼接的结果赋值给新的变量
            *= ： 将重复的指定次数赋值给新的变量
        3. 比较运算符：
            > >= < <= == !=
            规则：依据字符串中的Unicode编码依次比较两个字符串相对应位
                上的编码值的大小
        4. 成员运算符：
            判断某个值或元素是否存在于序列中, 存在返回True；否则返回False
            对象 in 序列
            对象 not in 序列


"""

a = 'hello'
b = 'world'
print(a + b)
print(a * 3)

a += b
print(a)
b *= 4
print(b)

# 3. 比较运算符
print(ord('a'))  # 97
print(ord('b'))  # 98
print('a' == 'b')
print('a' > 'b')
print('a' < 'b')
print('aa' == 'ab')

# 4. 成员运算符
info = "welcome to China"
print('w' in info)
print('to' in info)
print('Come' in info)
print('Come' not in info)
