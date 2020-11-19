""" Producers serving  for consumers """
from multiprocessing.managers import BaseManager
import multiprocessing as mp

queue = mp.Queue(20)


class QueueManager(BaseManager):
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
