"""
僵尸进程  ps -aux   stat ---> Z
僵尸处理：
子进程变成僵尸，父进程如果结束系统会处理僵尸
join()   主动回收子进程，释放资源
start()  创建新进程前会检测之前是否已经有僵尸，有则处理掉
"""

from multiprocessing import Process
from time import sleep
import os

def func():
    print("一大波僵尸正在接近",os.getpid())

# jobs = []
for i in range(5):
    p = Process(target = func)
    # jobs.append(p)
    p.start()
    sleep(1)

# [i.join() for i in jobs]

sleep(1000)
