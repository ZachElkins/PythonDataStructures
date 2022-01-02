import pytest
from data_structures.stack import Stack


def test_stack_init():
    stack = Stack()
    assert isinstance(stack, Stack)


def test_stack_init_from_list():
    stack = Stack([1, 2, 3])
    assert isinstance(stack, Stack)
    assert stack.size() == 3


def test_stack_init_error():
    with pytest.raises(TypeError):
        _ = Stack((1, 2, 3))


def test_stack_empty():
    stack = Stack()
    assert stack.empty() is True


def test_stack_push():
    stack = Stack()
    stack.push(1)
    assert stack.empty() is False
    assert stack.pop() == 1


def test_stack_peek():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1
    assert stack.empty() is False


def test_stack_peek_lookup_error():
    stack = Stack()
    with pytest.raises(LookupError):
        stack.peek()


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.empty() is True


def test_stack_pop_lookup_error():
    stack = Stack()
    with pytest.raises(LookupError):
        _ = stack.pop()


def test_stack_size():
    stack = Stack()
    assert stack.size() == 0
    stack.push(1)
    assert stack.size() == 1
    stack.pop()
    assert stack.size() == 0
