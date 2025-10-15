# from multiprocessing import Process
# import os
# import time

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

# processes = []
# num_processes = os.cpu_count()
# print(num_processes)

# #create processes
# for i in range(num_processes):
#     p = Process(target=square_numbers)
#     processes.append(p)

# #start each process
# for p in processes:
#     p.start()

# # join processes
# for p in processes:
#     p.join()  #waits for a process to finish, while waiting it is blocking the main thread

# print('end main')


# ----------------------------------
from threading import Thread
import os
import time

threads = []
num_threads = 10

for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print('end main')