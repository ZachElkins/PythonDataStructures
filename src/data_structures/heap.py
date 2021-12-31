
class Heap:
    def __init__(self, items=None):
        """Initialize the heap as empty"""
        if items is None:
            items = []
        self.items = items

        if not self.empty():
            self.build_heap()

    @staticmethod
    def parent_index(index): return (index-1)//2

    @staticmethod
    def left_index(index): return 2*index+1

    @staticmethod
    def right_index(index): return 2*index+2

    @staticmethod
    def has_parent(index): return Heap.parent_index(index) >= 0

    def has_left(self, index): return self.left_index(index) < self.size()

    def has_right(self, index): return self.right_index(index) < self.size()

    def swap(self, ia, ib):
        self.items[ia], self.items[ib] = self.items[ib], self.items[ia]

    def push(self, item):
        self.items.append(item)
        self.heapify_up()

    def pop(self):
        item = self.items[0]
        self.items[0] = self.items[self.size()-1]
        self.items = self.items[:-1]
        self.heapify_down()
        return item

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def empty(self):
        return self.size() == 0

    def get_heap(self):
        return self.items

    def heapify_up(self):
        index = self.size() - 1
        while all([
            self.has_parent(index),
            self.items[Heap.parent_index(index)] > self.items[index]
        ]):
            pi = self.parent_index(index)
            self.swap(index, pi)
            index = pi

    def heapify_down(self):
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
        idx = self.size()
        while idx >= 0:
            self.heapify(idx)
            idx = idx - 1
