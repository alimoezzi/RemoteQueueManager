import multiprocessing
from multiprocessing.managers import BaseManager
from multiprocessing import Process, current_process, Lock
import time


class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
QueueManager.register('get_max')
QueueManager.register('get_cnt')

num_producer = 2
pencil = Lock()

def producer(r_manger):
    r_manger.connect()
    serving_line = r_manger.get_queue()
    size = r_manger.get_max().get("size")
    i = r_manger.get_cnt()
    while True:
        with pencil:
            print(
                f'{current_process().name} produced #{i.value()} - remaining capacity: {size - serving_line.qsize()}')
            serving_line.put(f"Bowl #{i.value()}")
            i.increment()
            # sleep can represent that the thread is doing some io task
        time.sleep(0.2)


if __name__ == '__main__':
    m = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
    for i in range(num_producer):
        Process(target=producer, args=(m,), name=f'Producer {i}').start()
