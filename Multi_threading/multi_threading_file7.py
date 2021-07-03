# to get names of own defined threads

from threading import Thread


class x(Thread):
    def run(self):
        print(self.getName())


class y(Thread):

    def run(self):
        print(self.getName())



x1 = x()
x1.start()
y1 = y()
y1.start()


# default names of threads are Thread-1, Thread-2
