import pytest
from data_structures.stack import Stack


def test_stack_init():
    stack = Stack()
    assert type(stack) == Stack


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
    assert stack.pop() == 1
    assert stack.empty() is True


def test_stack_pop_lookup_error():
    stack = Stack()
    with pytest.raises(LookupError):
        _ = stack.pop()
