"""
select IO多路复用方法
"""
from select import select
from socket import *
from time import sleep

# 　创建几个套接字对象
tcp = socket()
tcp.bind(("0.0.0.0", 8888))
tcp.listen(5)

udp = socket(AF_INET, SOCK_DGRAM)

sleep(4)
print("开始监控ＩＯ对象")
rs, ws, xs = select([tcp,udp], [udp], [])
print("rlist:", rs)
print("wlist:", ws)
print("xlist:", xs)
