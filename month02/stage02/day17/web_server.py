"""
1. 使用类搭建 epoll tcp网络并发
2. 具体完成 http请求响应
"""
from socket import *
from select import *

# 具体处理实现http请求事务
class Handle:
    def __init__(self,html):
        self.html = html # 网页存放位置

    def get_info(self,conn):
        request = conn.recv(1024)
        if not request:
            return
        info = request.decode().split(' ')[1]
        return info

    # 发送响应
    def send_response(self,conn,info):
        pass


    def main(self,conn):
        # 接收http请求，解析除请求内容
        info = self.get_info(conn)
        if info:
            # 组织响应发送
            self.send_response(conn,info)


class WebServer:
    def __init__(self, host="", port=0,html=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.html = html # 网页存放位置
        self.sock = self._create_socket()
        self.ep = epoll()
        self.map = {}  # 查找字典
        self.handle = Handle(html)

    # 　创建监听套接字
    def _create_socket(self):
        sock = socket()
        sock.bind(self.address)
        sock.setblocking(False)  # 配合非阻塞，防止系统网络产生的延迟
        return sock

    # 　处理连接
    def _connect_client(self, fd):
        conn, addr = self.map[fd].accept()
        conn.setblocking(False)
        # 添加关注
        self.ep.register(conn, EPOLLIN)
        self.map[conn.fileno()] = conn

    # 启动网络服务
    def start(self):
        self.sock.listen(5)
        self.ep.register(self.sock)
        self.map[self.sock.fileno()] = self.sock
        print("Listen the port %d" % self.port)
        # 循环监控IO发生
        while True:
            events = self.ep.poll()
            for fd, event in events:
                if fd == self.sock.fileno():
                    self._connect_client(fd)
                else:
                    # 另外一个类的方法
                    self.handle.main(self.map[fd])


if __name__ == '__main__':
    web = WebServer(host="0.0.0.0", port=8000,html="./static")
    web.start()
