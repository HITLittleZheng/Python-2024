"""
字节串数据类型
字节串可以 + 拼接,空字节串为假非空为真

所有的字符串都能转换为字节串    是的
所有的字节串都能转换为字符串    不是
"""

# 英文字符字节串
byte01 = b"hello"
print(type(byte01))
print(byte01)

# 带有非英文字符需要通过encode() 转换
byte02 = "你好".encode()
print(byte02)

# 字节串 转换回字符串
print(byte02.decode())
print(b'\xe6\xb6\xa3\xc2\xb2\xbd'.decode())
