from threading import Thread
# Thread is a class inside threading module, helps to enable multi threading


class x(Thread):   # inheriting from Thread class

    def run(self):   # overriding run method with our requirement
        for i in range(1, 101):
            print(i)


class y(Thread):

    def run(self):
        for j in range(101, 201):
            print(j)

# creating objects and accessing the run method

x1 = x()
x1.start()# we have to call start() method to access run method() in Thread calss
y1 = y()
y1.start()


# in case we have more code (outside Thread)

for k in range(201, 301):
    print(k)    # this code is running in main thread along with own defined threads
