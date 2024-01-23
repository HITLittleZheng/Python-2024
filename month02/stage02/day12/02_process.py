"""
进程基础示例
"""

import multiprocessing as mp
from time import sleep

a = 1

# 进程执行函数
def func():
    print("开始执行一个进程任务")
    sleep(3)  # 模拟执行时间
    print("进程任务执行完成")
    global a
    print("a =",a)
    a = 10000

# 实例化进程对象
process = mp.Process(target=func)

# 启动进程 : 进程产生 --》 执行func
process.start()

print("我也干点事嘿嘿")
sleep(4)
print("我也干完啦，哈哈")

process.join() # 等待子进程完成
print("a :",a) # 1
