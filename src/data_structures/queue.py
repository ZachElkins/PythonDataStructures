from data_structures.stack import Stack


class Queue(Stack):
    """
    A class for a first-in-first-out data structure.
    Implemented using the data_structures.stack.Stack class.
    ...
    Methods
    _______
    push(item):
        Adds the item to the top of the queue.
    pop():
        Removes and returns the item from the start of the queue.
    peek():
        Returns the item from the start of the queue.
    empty():
        Returns True if the queue is empty, otherwise False.
    size():
        Returns size of the queue.
    """

    def push(self, item):
        """ Adds a new item to the top of the queue.
        :param item: The new item to add to the queue.
        """
        self.items = self.items + [item]
