
class Stack:
    """
    A class for a first-in-last-out data structure.
    ...
    Methods
    _______
    push(item):
        Adds the item to the top of the stack.
    pop():
        Removes and returns the top item the stack.
    peek():
        Returns the item on top of the stack.
    empty():
        Returns True if the stack is empty, otherwise False.
    size():
        Returns size of the stack.
    """

    def __init__(self):
        """Initializes the stack to an empty list."""
        self.items = []

    def push(self, item):
        """
        Adds a new item to the top of the stack.
        :param item: The new item to add to the stack.
        """
        self.items = [item] + self.items

    def pop(self):
        """
        Removes and returns the top item the stack.
        :return: Returns the next item in the stack.
        """
        if self.empty():
            raise LookupError("The stack is empty.")
        item = self.items[0]
        self.items = self.items[1:]
        return item

    def peek(self):
        """
        Returns the item on top of the stack.
        :return: The next item in the stack.
        """
        if self.empty():
            raise LookupError("The stack is empty.")
        return self.items[0]

    def empty(self):
        """
        Returns True if the stack is empty, otherwise False.
        :return: True if empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the size of the stack
        :return: Size of the stack
        """
        return len(self.items)
