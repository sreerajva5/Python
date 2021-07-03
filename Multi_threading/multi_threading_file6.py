from threading import Thread
# Thread is a class inside threading module, helps to enable multi threading


class x(Thread):   # inheriting from Thread class

    def run(self):   # overriding run method with our requirement
        for i in range(1, 101):
            print(i)



x1 = x()
x1.start()
x2 = x()
x2.start()
