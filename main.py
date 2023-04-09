from threading import Thread
from threading import Semaphore
from time import sleep
from random import random

n = 0
b = 0
g = 0
b_range = 0
g_range = 0
sleep_time = 0.5


def deduct_color(set_num, color, semaphore):
    global b, g, sleep_time
    with semaphore:
        match color:
            case "b":
                i = 0
                print("Blue only.")
                value = random()
                while (b > 0) & (i < n):
                    i = i + 1
                    b = b - 1
                print("Empty fitting room blue: {} green: {} Set thread: {}\n".format(b, g, set_num))
                sleep(value)

            case "g":
                i = 0
                print("Green only.")
                value = random()
                while (g > 0) & (i < n):
                    i = i + 1
                    g = g - 1
                print("Empty fitting room blue: {} green: {} Set thread: {}\n".format(b, g, set_num))
                sleep(value)


def create_color_threads():
    global b_range, g_range, n

    threads_tuple = []
    last_i = 0
    last_j = 0
    for i in range(int(b_range / n)):
        threads_tuple.append((i, "b"))
        last_i = i

    for j in range(int(g_range / n)):
        threads_tuple.append((last_i + (j + 1), "g"))
        last_j = last_i + (j + 1)

    if b_range % n > 0:
        threads_tuple.append((last_j + 1, "b"))
        if g_range % n > 0:
            threads_tuple.append((last_j + 2, "g"))
    elif g_range % n > 0:
        threads_tuple.append((last_j + 1, "g"))

    return threads_tuple


def perform_transactions(slots, blue, green):
    global n, b, g, b_range, g_range
    n = slots
    b = blue
    b_range = blue
    g = green
    g_range = green
    # starting processes
    threads_tuple = create_color_threads()

    for i in range(len(threads_tuple)):
        thread_tuple = threads_tuple[i]
        worker = Thread(target=deduct_color, args=(thread_tuple[0], thread_tuple[1], Semaphore(1)))
        worker.start()


if __name__ == "__main__":
    # x, y, z = input("Enter three values (n, b, g): ").split()
    # n = int(x)
    # b = int(y)
    # g = int(z)
    perform_transactions(6, 52, 20)
