""" Producers serving  for consumers """
from multiprocessing.managers import BaseManager
import multiprocessing as mp

queue = mp.Queue(20)


class QueueManager(BaseManager):
    pass


if __name__ == '__main__':
    # normally consuming  takes 0.1 longer than producing it so producer might add  a full queue!
    # also we should notify consumer that queue is empty
    # for cpu intensive work as of GIL there's no simultaneous threads so they can not consume as fast as producer does
    # here we need to use multiprocessing
    QueueManager.register('get_queue', lambda: queue)
    QueueManager.register('get_max', lambda: {"size": queue._maxsize})
    manager = QueueManager(address=('localhost', 50000), authkey=b'abracadabra')
    server = manager.get_server()
    server.serve_forever()
