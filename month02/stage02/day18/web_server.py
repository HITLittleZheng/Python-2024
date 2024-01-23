"""
1. 使用类搭建 epoll tcp网络并发
2. 具体完成 http请求响应
"""
from socket import *
from select import *


# 具体处理实现http请求事务
class Handle:
    def __init__(self, html):
        self.html = html  # 网页存放位置

    def get_info(self, conn):
        request = conn.recv(1024)
        if not request:
            return
        # 解析出 请求行 --》 请求内容
        info = request.decode().split(' ')[1]
        return info

    # 发送响应
    def send_response(self, conn, info):
        # 请求内容info ： 存在（/  网页名）  不存在
        if info == "/":
            info = "/index.html"
        try:
            fr = open(self.html + info, 'rb')
        except:
            with open(self.html + "/404.html", 'rb') as fr:
                data = fr.read()
            response = self._response("404 Not Found",data)
        else:
            response = self._response("200 OK",fr.read())
            fr.close()
        finally:
            conn.send(response)

    def _response(self,status, data):
        response = "HTTP/1.1 %s\r\n"%status
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response = response.encode() + data
        return response

    def main(self, conn):
        # 接收http请求，解析除请求内容
        info = self.get_info(conn)
        print("请求内容:", info)
        if info:
            # 组织响应发送
            self.send_response(conn, info)


# 搭建IO并发网络模型
class WebServer:
    def __init__(self, host="", port=0, html=None):
        self.host = host
        self.port = port
        self.address = (host, port)
        self.html = html  # 网页存放位置
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
        self.ep.register(self.sock,EPOLLIN)
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
                    self.map[fd].close()
                    self.ep.unregister(fd)
                    del map[fd]


if __name__ == '__main__':
    web = WebServer(host="0.0.0.0", port=8000, html="./static")
    web.start()
