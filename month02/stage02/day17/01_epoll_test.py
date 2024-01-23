"""
epoll IO多路复用方法
"""
from select import *
from socket import *
from time import sleep

# 　创建几个套接字对象
tcp = socket()
tcp.bind(("0.0.0.0", 8888))
tcp.listen(5)

udp = socket(AF_INET, SOCK_DGRAM)

ep = epoll() # 创建好epoll

# {fileno:object} 时刻与关注IO保持一直
map = {tcp.fileno():tcp}

ep.register(tcp,EPOLLIN) # 关注IO
ep.register(udp,EPOLLOUT) # 关注IO
map[udp.fileno()] = udp # 添加到字典

sleep(5)
print("开始监控ＩＯ对象")
events = ep.poll() # [(3,1)]
print(events)
# print(map[events[0][0]])



