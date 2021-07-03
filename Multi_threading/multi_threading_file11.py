# execute one thread with output or condition of another thread

from threading import Thread

class x(Thread):
    # find sum of numbers from 1 to 100
    def run(self):
        self.s = 0
        for i in range(1,101):
            self.s += i
            

class y(Thread):

    def __init__(self, x1):  # to connect between x and y classes. x1 will be an instance of x class.
        self.x1 = x1
        super().__init__() # super() function helps to get both parent and child class init method

    def run(self):
        for j in range(101, 201):
            print(j)
            if j == 150:
                self.x1.join() # join() methodstops execution of current thread util specified thread is over
                print(self.x1.s)



x1 = x()
x1.start()
y1 = y(x1)
y1.start()
