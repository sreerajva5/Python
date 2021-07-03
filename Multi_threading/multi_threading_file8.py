# delay execution of thread

from threading import Thread
import time

class x(Thread):
    def run(self):
        time.sleep(10)
        for i in range(1,101):
            print(i)


class y(Thread):

    def run(self):
        for j in range(101, 201):
            print(j)



x1 = x()
x1.start()
y1 = y()
y1.start()
