"""
练习：
通过浏览器访问  127.0.0.1:8000可以获取一张图片
图片自定，要求可以循环的访问

提示： Content-Type:image/jpeg
"""
from socket import *

sock = socket()
sock.bind(("0.0.0.0",8000))
sock.listen(5)

while True:
    # 浏览器每次访问都重新连接
    conn,addr = sock.accept()
    print("Connect from",addr)
    # 不在乎请求是什么
    request = conn.recv(1024)
    # 组织响应
    response = b"HTTP/1.1 200 OK\r\n"
    response += b"Content-Type:image/jpeg\r\n"
    response += b"\r\n"
    with open("sj.jpg",'rb') as file:
        response += file.read()
    conn.send(response) # 发送响应
