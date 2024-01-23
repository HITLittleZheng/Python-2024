"""
父进程中创建多个子进程
"""
from multiprocessing import Process
import os
from time import sleep

# def th1():
#     sleep(4)
#     print("吃饭")
#     print(os.getppid(),"--",os.getpid())
#
# def th2():
#     sleep(2)
#     print("睡觉")
#     print(os.getppid(),"--",os.getpid())
#
# def th3():
#     sleep(3)
#     print("打豆豆")
#     print(os.getppid(),"--",os.getpid())

# 循环创建进程
# jobs = [] # 存储进程对象
# for th in [th1,th2,th3]:
#     p = Process(target=th)
#     jobs.append(p) # 保存进程对象
#     p.start()

############### 如果只用一个函数 ###########

# 统一的进程函数
def th(sec,info):
    sleep(sec)
    print(info)
    print(os.getppid(),"--",os.getpid())

# 循环创建进程
jobs = [] # 存储进程对象
for args in [(4,"吃饭"),(2,"睡觉"),(3,"打豆豆")]:
    p = Process(target=th,args=args)
    jobs.append(p) # 保存进程对象
    p.start()


#########################################


# 判定所有子进程结束 [i.join() for i in jobs]
for i in jobs:
    i.join()

print("所有事情都完成啦")








