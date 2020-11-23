from multiprocessing.managers import BaseManager
from multiprocessing import Process
import time


class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
QueueManager.register('get_max')

num_producer = 2

def producer(r_manger):
    i = 1
    r_manger.connect()
    serving_line = r_manger.get_queue()
    size = r_manger.get_max().get("size")
    while True:
        print(
            f'Served {i % size} - remaining capacity: {size - serving_line.qsize()}')
        serving_line.put(f"Bowl #{i % size}")
        i += 1
        # sleep can represent that the thread is doing some io task
        time.sleep(0.2)


if __name__ == '__main__':
    m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
    for i in range(num_producer):
        Process(target=producer, args=(m,), name=f'Producer {i}').start()
