import pytest
from data_structures.heap import Heap


@pytest.fixture
def base_heap():
    heap = Heap()
    heap.push(1)
    heap.push(2)
    heap.push(3)
    heap.push(4)
    heap.push(5)
    return heap


def test_heap_init():
    basic_heap = Heap()
    init_list_heap = Heap([9, 8, 7, 5, 1, 2])
    assert isinstance(Heap, basic_heap)
    assert isinstance(Heap, init_list_heap)


def test_heap_push():
    heap = Heap()
    heap.push(2)
    heap.push(3)
    heap.push(1)


def test_heap_pop(base_heap):
    assert base_heap.pop() == 1
    assert base_heap.pop() == 2


def test_heap_peek(base_heap):
    assert base_heap.peek() == 1


def test_heap_empty():
    heap = Heap()
    assert heap.empty()
    heap.push(1)
    assert not heap.empty()


def test_heapify_up_and_down(base_heap):
    base_heap.pop()
    base_heap.pop()
    base_heap.push(8)
    base_heap.push(1)
    base_heap.push(0)
    base_heap.push(9)
    assert base_heap.get_heap() == [0, 3, 1, 8, 4, 5, 9]


def test_heapify():
    heap = Heap([8, 9, 5, 1, 3, 2, 0, 6])
    assert heap.get_heap() == [0, 1, 2, 6, 3, 8, 5, 9]
