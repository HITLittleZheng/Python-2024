"""
自己定义一个线程类
"""
from threading import Thread
from time import sleep

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__(daemon = True)


    def run(self):
        for i in range(3):
            print("播放:",self.song)
            sleep(2)

t = MyThread("凉凉")
t.start()