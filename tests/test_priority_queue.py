from data_structures.priority_queue import PriorityQueue


def test_priority_queue_init():
    pq = PriorityQueue(lambda x: x[1])
    assert isinstance(pq, PriorityQueue)


def test_priority_queue_init_from_list():
    lst = [5, 2, 1, 4, 0]
    pq = PriorityQueue(items=lst)
    assert pq.pop() == 0
    assert pq.pop() == 1
    assert pq.peek() == 2


def test_priority_queue_push():
    pq = PriorityQueue(lambda x: x[1])
    small = [3, 1]
    medium = [2, 3]
    large = [1, 5]
    pq.push(large)
    pq.push(small)
    pq.push(medium)

    assert pq.size() == 3
    assert pq.peek() == small


def test_priority_queue_no_sort_fn():
    pq = PriorityQueue()
    pq.push(2)
    pq.push(1)
    pq.push(5)
    pq.push(0)
    assert pq.pop() == 0
    assert pq.pop() == 1
    assert pq.peek() == 2


def test_priority_queue_reverse_sort():
    pq = PriorityQueue(reverse=True)
    pq.push(0)
    pq.push(5)
    pq.push(2)
    pq.push(1)
    assert pq.pop() == 5
    assert pq.pop() == 2
    assert pq.peek() == 1
