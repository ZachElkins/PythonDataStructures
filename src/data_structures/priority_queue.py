from data_structures.queue import Queue


class PriorityQueue(Queue):
    """
    Implementation of a priority queue using the Queue class.
    ...
    Methods
    _______
    push(item):
        Adds the item to its sorted position of the queue.
    pop():
        Removes and returns the item from the start of the queue.
    peek():
        Returns the item from the start of the queue.
    empty():
        Returns True if the queue is empty, otherwise False.
    size():
        Returns size of the queue.
    """

    def __init__(self, sort_fn=None, items=None, reverse=False):
        """
        Initialize the priority queue and sorts any default value provided
        :param sort_fn: Key function used to sort the queue
        :param reverse: Default sort if False, reverse sort if True
        """
        super().__init__(items)
        self.reverse = reverse
        self.sort_fn = sort_fn
        if not self.empty():
            self.sort()

    def sort(self):
        """Sorts the queue based on the sort function"""
        self.items.sort(key=self.sort_fn, reverse=self.reverse)

    def push(self, item):
        """
        Pushed the new item in to the queue and sorts it
        :param item: Item to be added to the queue
        """
        super().push(item)
        self.sort()
