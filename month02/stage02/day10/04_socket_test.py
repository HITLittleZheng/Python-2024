"""
创建一个套接字对象
"""
import socket

# 创建udp套接字对象
udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 绑定地址
udp_socket.bind(("0.0.0.0",8888))







