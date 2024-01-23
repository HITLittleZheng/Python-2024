"""
基于　ｓｅｌｅｃｔ 方法的ＩＯ网络并发
重点代码 ！
"""
from socket import *
from select import select

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

#　ＩＯ监控列表
rlist = [sock]
wlist = []
xlist = []

while True:
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r == sock:
            #　处理连接
            conn,addr = r.accept()
            print("Connect from",addr)
            conn.setblocking(False)
            rlist.append(conn) # 添加关注
        else:
            # 　与客户端交互
            data = r.recv(1024)
            if not data:
                rlist.remove(r) #　客户端退出
                r.close()
                continue
            print("收到:", data.decode())
            r.send(b'Thanks')
    #         wlist.append(r) # 关注写
    #
    # for w in ws:
    #     w.send(b"OK")
    #     wlist.remove(w)