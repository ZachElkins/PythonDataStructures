from data_structures.queue import Queue


def test_queue_init():
    queue = Queue()
    assert isinstance(queue, Queue)


def test_queue_push():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    assert queue.empty() is False
    assert queue.pop() == 1
