from multiprocessing import Process, Value, Array, Lock
import os
import time
from multiprocessing import Queue
from multiprocessing import Pool

# def square_numbers():
#     for i in range(1000):
#         i * i

def add_100(number, lock):
    for i in range(100):
        # time.sleep(0.01)
        # lock.acquire()
        # number.value += 1
        # lock.release()

        time.sleep(0.01)
        with lock:
            number.value += 1

def add_100_arr(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1.0

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)
    
def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)

def cube(number):
    return number * number * number

if __name__ == "__main__":
    # # processes = []
    # # num_processes = os.cpu_count()
    # # # number of CPUs on the machine. Usually a good choice for the number of processes

    # # # create processes and assign a function for each process
    # # for i in range(num_processes):
    # #     process = Process(target=square_numbers)
    # #     processes.append(process)
    
    # # # start all processes
    # # for process in processes:
    # #     process.start()
    
    # # #wait for all processes to finish
    # # #block the main program until these processes are finished
    # # for process in processes:
    # #     process.join()

    # lock = Lock()
    # shared_number = Value('i', 0)
    # print('Number at beginning is', shared_number.value)
    # shared_array = Array('d', [0.0, 100.0, 200.0])
    # print('Array at beginning is', shared_array[:])
    # p1 = Process(target=add_100, args=(shared_number,lock))
    # p2 = Process(target=add_100, args=(shared_number,lock))
    # processes = []
    # for i in range(2):
    #     process_temp = Process(target=add_100, args=(shared_number, lock))
    #     processes.append(process_temp)
    # for proc in processes:
    #     proc.start()
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # for proc in processes:
    #     proc.join()
    # print('number at end is', shared_number.value)
    # p3 = Process(target=add_100_arr, args=(shared_array,lock))
    # p4 = Process(target=add_100_arr, args=(shared_array,lock))
    # p3.start()
    # p4.start()
    # p3.join()
    # p4.join()
    # print('array at end is', shared_array[:])
    
    # numbers = range(1, 6)
    # q = Queue()
    # p1 = Process(target=square, args=(numbers,q))
    # p2 = Process(target=make_negative, args=(numbers,q))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()
    # while not q.empty():
    #     print(q.get())
    
    pool = Pool()
    numbers = range(10)
    #map, apply, join, close
    result = pool.map(cube, numbers)
    # pool.apply(cube, numbers[0])
    pool.close()
    pool.join()
    print(result)
