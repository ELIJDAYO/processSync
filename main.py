from threading import *
from time import sleep

n = 0
b = 0
g = 0
b_range = 0
g_range = 0
sleep_time = 1
semaphore = Semaphore(1)


def deduct_blue(set_num, thread_num):
    global b, g
    if b > 0:
        b = b - 1
        print("blue {}->{} green {} Thread-{} Set-{}: ".format(b + 1, b, g, thread_num, set_num, ))
        sleep(sleep_time)


def deduct_green(set_num, thread_num):
    global b, g
    if g > 0:
        g = g - 1
        print("blue: {} green: {}->{} Thread-{} Set-{}: ".format(b, g + 1, g, thread_num, set_num,))
        sleep(sleep_time)


def create_blue_thread(set_num):
    global sleep_time, semaphore, n
    for i in range(n):
        semaphore.acquire()
        # sleep(sleep_time)
        if i == 0:
            print("Blue only")
        worker = Thread(target=deduct_blue, args=[set_num, i])
        worker.start()
        semaphore.release()
        if i == n-1:
            print("Empty fitting room")


def create_green_thread(set_num):
    global sleep_time, semaphore, n
    for i in range(n):
        semaphore.acquire()
        # sleep(sleesp_time)
        if i == 0:
            print("Green only\n")
        worker = Thread(target=deduct_green, args=[set_num, i])
        worker.start()
        semaphore.release()
        if i == n-1:
            print("Empty fitting room\n")


def create_color_threads():
    global b_range, g_range, n

    threads = []
    last_i = 0
    last_j = 0
    for i in range(int(b_range / n)):
        last_i = i
        threads.append(Thread(target=create_blue_thread, args=[last_i]))

    for j in range(int(g_range / n)):
        last_j = last_i + (j + 1)
        threads.append(Thread(target=create_green_thread, args=[last_j]))

    if b_range % n > 0:
        threads.append(Thread(target=create_blue_thread, args=[last_j + 1]))
        if g_range % n > 0:
            threads.append(Thread(target=create_green_thread, args=[last_j + 2]))
    elif g_range % n > 0:
        threads.append(Thread(target=create_green_thread, args=[last_j + 1]))

    return threads


def perform_transactions(slots, blue, green):
    global n, b, g, b_range, g_range
    n = slots
    b = blue
    b_range = blue
    g = green
    g_range = green
    # starting processes
    threads = create_color_threads()

    for i in range(len(threads)):
        worker = threads[i]
        # sleep(sleep_time)
        worker.start()


if __name__ == "__main__":
    # x, y, z = input("Enter three values (n, b, g): ").split()
    # n = int(x)
    # b = int(y)
    # g = int(z)
    perform_transactions(6, 20, 50)
