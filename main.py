import multiprocessing
import os
from threading import *
import time

n = 0
b = 0
g = 0
obj = Semaphore(n)


# function to withdraw from account
def deduct_blue():
    global b, obj
    i = 0
    obj.acquire()
    print("Blue only.")
    while (b > 0) & (i < n):
        i = i + 1
        b = b - 1
    print("Empty fitting room blue: {} green: {} pid: {}".format(b, g, os.getpid()))
    time.sleep(4)
    obj.release()


# function to deposit to account
def deduct_green():
    global g, obj
    i = 0
    obj.acquire()
    print("Green only.")
    while (g > 0) & (i < n):
        i = i + 1
        g = g - 1
    print("Empty fitting room blue: {} green: {} pid: {}".format(b, g, os.getpid()))
    time.sleep(4)
    obj.release()


def create_threads():
    # creating new processes
    p1 = Thread(target=deduct_blue, args=())
    p2 = Thread(target=deduct_green, args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()


def perform_transactions(slots, blue, green):
    global n, b, g, obj
    n = slots
    b = blue
    g = green
    obj = Semaphore(n)

    # starting processes
    while b + g > 0:
        create_threads()


if __name__ == "__main__":
    # x, y, z = input("Enter three values (n, b, g): ").split()
    # n = int(x)
    # b = int(y)
    # g = int(z)
    perform_transactions(6, 8, 20)
