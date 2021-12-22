
class TreeNode:
    """A class representing a node for any type of tree data structure."""

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, left):
        if not isinstance(left, TreeNode) and left is not None:
            raise TypeError(f"Children must be of type TreeNode, not {type(left)}, {type(self)}.")
        self._left = left

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        if not isinstance(right, TreeNode) and right is not None:
            raise TypeError(f"Children must be of type TreeNode, not {type(right)}.")
        self._right = right

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            raise TypeError(f"No comparison between TreeNode and {type(other)}, {other}")
        return self._data == other.data

    def __lt__(self, other):
        if not isinstance(other, TreeNode):
            raise TypeError(f"No comparison between TreeNode and {type(other)}")
        return self._data < other.data

    def __le__(self, other):
        if not isinstance(other, TreeNode):
            raise TypeError(f"No comparison between TreeNode and {type(other)}")
        return self._data <= other.data

    def __gt__(self, other):
        if not isinstance(other, TreeNode):
            raise TypeError(f"No comparison between TreeNode and {type(other)}")
        return self._data > other.data

    def __ge__(self, other):
        if not isinstance(other, TreeNode):
            raise TypeError(f"No comparison between TreeNode and {type(other)}")
        return self._data >= other.data
