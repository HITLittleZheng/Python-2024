"""
    字符串常用方法
"""

# ''.isdigit() 判断字符串是否全为数字
print('123'.isdigit())
print('123a'.isdigit())

# ''.upper() 转大写
# ''.lower() 转小写
print('abAdefg'.upper())
print('aAcdEfg'.lower())

# ''.isalpha() 是否为全字母
print('123456abc'.isalpha())
print('123456'.isalpha())

# ''.isalnum() 字符串中至少有一个字符且所有字符都是字母和数字
print(''.isalnum())
print('abc_'.isalnum())
print('123456'.isalnum())

print('   123456  \n  '.lstrip())  # 去除左侧空格 left
print('   123456  \n  '.rstrip())  # 去除右侧空格 right
print('   123456  \n  '.strip())  # 去除两个空格  left + right
print('---')

# ''.replace(old, new, count) 替换
s = 'banana'
print(s.replace('a', 'A'))  # 默认全部替换
print(s.replace('a', 'A', 1))  # 从左至右替换一个
print(s.replace('B', 'A', 1))  # 字符不存在, 不替换
print(s.replace('a', 'A', 4))  # 后续无效
