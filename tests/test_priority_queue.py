from data_structures.priority_queue import PriorityQueue
from dataclasses import dataclass


@dataclass
class Rect:
    width: int
    height: int


def test_priority_queue_init():
    pq = PriorityQueue(lambda x: x.height)
    assert isinstance(pq, PriorityQueue)


def test_priority_queue_init_from_list():
    lst = [5, 2, 1, 4, 0]
    pq = PriorityQueue(items=lst)
    assert pq.pop() == 0
    assert pq.pop() == 1
    assert pq.peek() == 2


def test_priority_queue_push():
    pq = PriorityQueue(lambda x: x.height)
    small = Rect(width=1, height=1)
    medium = Rect(width=1, height=2)
    large = Rect(width=1, height=3)
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
