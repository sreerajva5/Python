from threading import Thread
import time

def doubles(numbers):  # consider numbers as a list
    for i in numbers:
        time.sleep(1)
        print(i*2)


def squares(numbers):  # consider numbers as a list
    for i in numbers:
        time.sleep(1)
        print(i**2)


n = [1, 2, 3, 4, 5]

start = time.time()

t1 = Thread(target=doubles, args=(n,))
t2 = Thread(target=squares, args=(n,))

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print('time tahen : ', end-start)
