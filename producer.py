

class QueueManager(BaseManager):
    pass


QueueManager.register('get_queue')
QueueManager.register('get_max')


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
        time.sleep(0.5)
