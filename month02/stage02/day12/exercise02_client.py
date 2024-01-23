"""
练习2 客户端
"""
from socket import *
from time import sleep

data = [
  "张三  18   177",
  "李四  19   180",
  "王五  120  183"
]

sock = socket()
sock.connect(("127.0.0.1",8880))

# 循环发送
# for row in data:
#     sock.send(row.encode())

# 一起发送  组织简单格式
rows = "\n".join(data)
sock.send(rows.encode())

sleep(0.1) # 延迟发送
sock.send(b"#") # 结束标志

sock.close()
