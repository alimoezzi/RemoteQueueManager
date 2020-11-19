class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
QueueManager.register('get_max')

def cpu_work(work_units):
    x = 0
    for w in range(work_units * 1_000_000):
        x += 1
