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

doubles(n)
squares(n)

end = time.time()

print('time tahen : ', end-start)
