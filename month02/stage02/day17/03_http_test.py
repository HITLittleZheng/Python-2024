"""
http 请求和响应
"""
from socket import *

# tcp套接字
sock = socket()
sock.bind(("0.0.0.0",8880))
sock.listen(5)

# 等待浏览器连接
conn,addr = sock.accept()
print("Connect from",addr)

# 接收浏览器 http 请求
data = conn.recv(1024)
print(data.decode())

response = """HTTP/1.1 200 OK
Content-Type:text/html

Hello world
"""
conn.send(response.encode()) # 发送响应

conn.close()
sock.close()
