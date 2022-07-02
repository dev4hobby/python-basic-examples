import time

# time now as 'hh:mm:ss' GMT+9
def print_time():
    a = time.strftime("%H:%M:%S", time.gmtime(time.time() + 9 * 60 * 60))
    print(a)


print_time()
