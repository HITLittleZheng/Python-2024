"""
非阻塞ＩＯ模型
"""
from socket import *
from time import sleep,ctime

log = open("my.log",'a',buffering=1) # 日志

#　创建ｔｃｐ监听套接字
sock = socket()
sock.bind(("0.0.0.0",8888))
sock.listen(5)

# 设置套接字非阻塞
# sock.setblocking(False)

#　设置一个超时时间
sock.settimeout(4)

while True:
    try:
        conn,addr = sock.accept()
        print("Connect from",addr)
    except BlockingIOError as e:
        #　干点和客户端连接无关的事情
        msg = "%s : %s\n"%(ctime(),e)
        log.write(msg)
        sleep(3)
    except timeout as e:
        # 干点和客户端连接无关的事情
        msg = "%s : %s\n" % (ctime(), e)
        log.write(msg)
    else:
        #  干点和客户端连接有关的事情
        data = conn.recv(1024)
        print(data.decode())




