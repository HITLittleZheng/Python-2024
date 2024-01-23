"""
    已知 s = 'ABCDEFG' 分别写出以下操作的值
    口诀：
        正向正切有值,否则为空
        反向反切有值,否则为空
"""

s = 'ABCDEFG'

print(s[3])  # 'D'
print(s[::])  # 'ABCDEFG'
print(s[2:])  # 'CDEFG'
print(s[:6])  # 'ABCDEF'
print(len(s))  # 7
print(s[-len(s):-2:-1])  # ''
print(s[-6:1:2])  # ''
