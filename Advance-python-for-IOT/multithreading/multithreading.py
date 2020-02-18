# from threading module, we need to import the Thread class for creating multithreading objects
from threading import Thread
import time


def f1(args):
    print("Hi from f1 with argument "+str(args))
    time.sleep(5)
    print("Hi,f1 woke up with argument "+str(args))


for i in range(10):
    t1 = Thread(target=f1, args=(i,))
    t1.start()


# t1 = Thread(target=f1)
# t1.start()
# print("Hi from main")
# time.sleep(5)
# print('Hi main got up')
# t1.join()
