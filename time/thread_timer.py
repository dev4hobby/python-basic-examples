import time
import threading


def print_time():
    a = time.strftime("%H:%M:%S")
    print(a)
    threading.Timer(1, print_time).start()


print_time()
