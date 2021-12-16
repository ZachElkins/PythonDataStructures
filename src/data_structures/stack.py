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
    """

    def __init__(self):
        """ Initializes the stack to an empty list."""
        self.stack = []

    def push(self, item):
        """ Adds a new item to the top of the stack.
        :param item: The new item to add to the stack.
        :return:
        """
        self.stack = [item] + self.stack

    def pop(self):
        """
        Removes and returns the top item the stack.
        :return:
        """
        if self.empty():
            raise LookupError("The stack is empty.")
        item = self.stack[0]
        self.stack = self.stack[1:]
        return item

    def peek(self):
        """
        peek():
            Returns the item on top of the stack.
        :return:
        """
        if self.empty():
            raise LookupError("The stack is empty.")
        return self.stack[0]

    def empty(self):
        """
        empty():
            Returns True if the stack is empty, otherwise False.
        :return:
        """
        return len(self.stack) == 0
