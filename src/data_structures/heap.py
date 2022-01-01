
class Heap:
    """
    A class implementing a heap data structure using a list
    ...
    Methods
    _______
    push(item):
        Add an item to the heap
    pop():
        Retrieve the smallest item, and remove it from the heap
    peek():
        Look at the next item in the heap
    size():
        Get the number of items in the heap
    empty():
        Check if the heap is empty
    get_heap():
        View the heap as a list
    """

    def __init__(self, items=None):
        """
        Initialize the heap as empty unless a list is already given
        :param items: List of items to initialize the heap
        """
        if items is None:
            items = []
        self.items = items

        if not self.empty():
            self.build_heap()

    @staticmethod
    def parent_index(index):
        """
        Get the given index's parent

        :param index: index to find parent of
        :return: Parent's index
        """
        return (index-1)//2

    @staticmethod
    def left_index(index):
        """
        Get the given index's left child

        :param index: index to find the left child or
        :return: Left child's index
        """
        return 2*index+1

    @staticmethod
    def right_index(index):
        """
        Get the given index's right child

        :param index: index to find the right child or
        :return: Right child's index
        """
        return 2*index+2

    @staticmethod
    def has_parent(index):
        """
        Check if the given index has a parent
        :param index: Index to check for a parent of
        """
        return Heap.parent_index(index) >= 0

    def has_left(self, index):
        """
        Check if the given index has a left child
        :param index: Index to check for a left child of
        """
        return self.left_index(index) < self.size()

    def has_right(self, index):
        """
        Check if the given index has a right child
        :param index: Index to check for a right child of
        """
        return self.right_index(index) < self.size()

    def swap(self, ia, ib):
        """
        Swap two elements in the heap
        :param ia: index of first element
        :param ib: index of second element
        """
        self.items[ia], self.items[ib] = self.items[ib], self.items[ia]

    def push(self, item):
        """
        Add an item to the heap
        :param item: item to add to the heap
        """
        self.items.append(item)
        self.heapify_up()

    def pop(self):
        """
        Retrieve the smallest item, and remove it from the heap
        :return: Smallest item in the heap
        """
        item = self.items[0]
        self.items[0] = self.items[self.size()-1]
        self.items = self.items[:-1]
        self.heapify_down()
        return item

    def peek(self):
        """Look at the next item in the heap"""
        return self.items[0]

    def size(self):
        """
        Get the number of items in the heap
        :return: Number of items in the heap
        """
        return len(self.items)

    def empty(self):
        """
        Check if the heap is empty
        :return: True if empty, False otherwise
        """
        return self.size() == 0

    def get_heap(self):
        """
        View the heap as a list
        :return: List containing the heap elements in order
        """
        return self.items

    def heapify_up(self):
        """Fix the heap from the bottom up"""
        index = self.size() - 1
        while all([
            self.has_parent(index),
            self.items[Heap.parent_index(index)] > self.items[index]
        ]):
            pi = self.parent_index(index)
            self.swap(index, pi)
            index = pi

    def heapify_down(self):
        """Fix the heap from the top down"""
        index = 0
        while self.has_left(index):
            smaller_idx = Heap.left_index(index)
            if self.has_right(index):
                ri = Heap.right_index(index)
                if self.items[ri] < self.items[smaller_idx]:
                    smaller_idx = ri

            self.swap(index, smaller_idx)
            index = smaller_idx

    def heapify(self, index):
        """
        Fix heap properties starting from given index
        :param index: Index to heapify from
        """
        smaller_idx = index

        if self.has_left(index):
            li = Heap.left_index(index)
            if self.items[li] < self.items[smaller_idx]:
                smaller_idx = li

        if self.has_right(index):
            ri = Heap.right_index(index)
            if self.items[ri] < self.items[smaller_idx]:
                smaller_idx = ri

        if smaller_idx != index:
            self.swap(index, smaller_idx)
            self.heapify(smaller_idx)

    def build_heap(self):
        """Create a proper heap from an unordered list"""
        idx = self.size()
        while idx >= 0:
            self.heapify(idx)
            idx = idx - 1
