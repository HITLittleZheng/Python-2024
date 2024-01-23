"""
基于epoll方法的ＩＯ网络并发
重点代码 ！
"""
from socket import *
from select import *

#　服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

#　创建监听套接字
sock = socket()
sock.bind(ADDR)
sock.listen(5)
sock.setblocking(False) # 配合非阻塞，防止系统网络产生的延迟
print("Listen the port %d"%PORT)

# 创建epoll对象
ep = epoll()
ep.register(sock,EPOLLIN) # 初始关注
#　查找字典　　ｆｉｌｅｎｏ--> object
map = {sock.fileno():sock}

while True:
    events = ep.poll() #　开始监控 [(fd,event),()...]
    print("你有新的IO需要处理哦",events)
    for fd,event in events:
        if fd == sock.fileno():
            #　处理连接
            conn,addr = map[fd].accept()
            print("Connect from",addr)
            conn.setblocking(False)
            # 添加关注 设置边缘触发
            ep.register(conn,EPOLLIN|EPOLLET)
            map[conn.fileno()] = conn #　维护字典
        # elif event == EPOLLIN:
        #     # 　与客户端交互
        #     data = map[fd].recv(1024)
        #     if not data:
        #         ep.unregister(fd) #　客户端退出
        #         map[fd].close()
        #         del map[fd] # 从字典删除
        #         continue
        #     print("收到:", data.decode())
        #     # map[fd].send(b'Thanks')
        #     ep.unregister(fd)
        #     ep.register(fd,EPOLLOUT)
        # elif event == EPOLLOUT:
        #     map[fd].send(b'OK')
        #     ep.unregister(fd)
        #     ep.register(fd, EPOLLIN)