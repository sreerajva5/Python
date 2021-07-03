# delay in between execution of thread

from threading import Thread
import time

class x(Thread):
    def run(self):
        
        for i in range(1,11):
            print(i)
            time.sleep(1)


class y(Thread):

    def run(self):
        time.sleep(5)
        for j in range(10, 16):
            print(j)



x1 = x()
x1.start()
y1 = y()
y1.start()
