from multiprocessing.managers import BaseManager
from multiprocessing import Process, current_process
import time
import random


class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
QueueManager.register('get_max')

num_consumer = 5


def cpu_work(work_units):
    x = 0
    for w in range(work_units * 1_000_000):
        x += 1


def consumer(r_manger):
    r_manger.connect()
    serving_line = r_manger.get_queue()
    while True:
        try:
            q = serving_line.get(timeout=10)
        except Exception as e:
            print(current_process().name, "exited")
            break
        print(current_process().name, "ate", q)
        # sleep can represent that the thread is doing some io task
        # to simulate cpu intensive work we can use for loops
        time.sleep(random.random())
        cpu_work(2)


if __name__ == '__main__':
    m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
    processes = [Process(target=consumer, args=(m,), name=f'Consumer {i}') for i in range(num_consumer)]
    for i in range(num_consumer):
        processes[i].start()
    for i in range(num_consumer):
        processes[i].join()
