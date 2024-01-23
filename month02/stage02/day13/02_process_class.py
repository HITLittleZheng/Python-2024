"""
进程类
"""
from multiprocessing import Process
from time import sleep

# 做好“干事”  做好创建进程
class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        # 拥有自己实例变量的同时也需要保留父类的
        super().__init__()

    # 进程要做的事情
    def run(self):
        for i in range(self.value):
            print("这是我要干的事情")
            sleep(2)
            print("干完了")


if __name__ == '__main__':
    myprocess = MyProcess(3)
    myprocess.start() # 独立的进程去做


# Process猜想

# class Process:
#     def __init__(self,target):
#         self._target = target
#
#     def run(self):
#         self._target()
#
#     def start(self):
#         创建进程
#         self.run()
#
#
# p = Process(target=func)
# p.start()