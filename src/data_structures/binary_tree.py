from data_structures.tree_node import TreeNode
from data_structures.queue import Queue
from data_structures.stack import Stack


class BinaryTree:
    """
    A class for binary tree, implemented
    using data_structures.tree_node.TreeNode.
    ...
    Methods
    _______
    insert(item):
        Adds a new TreeNode to the tree.
    traverse_inorder():
        Traverses the tree in in-order.
    traverse_preorder():
        Traverses the tree in pre-order.
    delete(key):
        Remove the node from the tree that matches the given key.
    bfs(key)
        Breadth-first search for the matching key.
    dfs(key)
        Depth-first search for the matching key.
    size()
        Returns the number of nodes in the tree.
    """

    def __init__(self, data):
        """
        Initialize the binary tree root from a piece of data or an
        already existing TreeNode.
        :param data: A piece of data or an existing TreeNode.
        """
        if isinstance(data, TreeNode):
            self.root = data
        else:
            self.root = TreeNode(data)

    def insert(self, data):
        """
        Adds a new TreeNode to the tree, smaller data flows to the left,
        larger data flows to the right.

        :param data: Data to put in the TreeNode at the bottom of the tree.
        """
        if data < self.root.data:
            if self.root.left is None:
                self.root.left = TreeNode(data)
            else:
                self.root.left.insert(data)
        else:
            if self.root.right is None:
                self.root.right = TreeNode(data)
            else:
                self.root.right.insert(data)

    def traverse_inorder(self):
        """
        Traverses the tree in-order.
        :return: A list representing the data at each node.
        """
        return BinaryTree.traverse_inorder_helper(self.root)

    @staticmethod
    def traverse_inorder_helper(root):
        """
        Static function to traverse the tree in in-order

        :param root: Root of the tree to traverse.
        :return: In-order traversal of subtree.
        """
        res = []
        if root:
            res = BinaryTree.traverse_inorder_helper(root.left)
            res.append(root.data)
            res = res + BinaryTree.traverse_inorder_helper(root.right)
        return res

    def traverse_preorder(self):
        """
        Traverses the tree in pre-order.

        :return: A list representing the data at each node.
        """
        return BinaryTree.traverse_preorder_helper(self.root)

    @staticmethod
    def traverse_preorder_helper(root):
        """
        Static function to traverse the tree in pre-order

        :param root: Root of the tree to traverse.
        :return: Pre-order traversal of subtree.
        """
        res = []
        if root:
            res.append(root.data)
            res = res + BinaryTree.traverse_preorder_helper(root.left)
            res = res + BinaryTree.traverse_preorder_helper(root.right)
        return res

    @staticmethod
    def delete_deepest(root, node):
        """
        Static function to delete a deep element.

        :param root: The root of the tree to search and delete from.
        :param node: Node to find and delete deepest of.
        """
        q = Queue()
        q.push(root)
        while not q.empty():
            current_node = q.pop()
            if current_node is node:
                return
            if current_node.right:
                if current_node.right is node:
                    current_node.right = None
                    return
                else:
                    q.push(current_node.right)
            if current_node.left:
                if current_node.left is node:
                    current_node.left = None
                    return
                else:
                    q.push(current_node.left)

    def delete(self, key):
        """
        Remove the node from the tree that matches the given key.

        :param key: Key to check for data in a node to delete.
        """
        return BinaryTree.delete_helper(self.root, key)

    @staticmethod
    def delete_helper(root, key):
        """
        Static function to delete an element.

        :param root: The root of the tree to search and delete from.
        :param key: Key to check for data in a node to delete.
        """

        # Not sure what to do in case where root is deleted and nothing remains
        # if root is None:
        #     return
        #
        # if root.left is None and root.right is None:
        #     if root.data == key:
        #         return
        #     else:
        #         return

        key_node = None
        q = Queue()
        q.push(root)
        while not q.empty():
            current_node = q.pop()
            if current_node.data == key:
                key_node = current_node
            if current_node.left:
                q.push(current_node.left)
            if current_node.right:
                q.push(current_node.right)

        if key_node:
            val = current_node.data
            BinaryTree.delete_deepest(root, current_node)
            key_node.data = val
        return

    def bfs(self, key):
        """
        Depth-first search for the matching key.

        :param key: Key to check for data in a node being searched for.
        :return: The TreeNode containing the key, else None.
        """
        q = Queue()
        q.push(self.root.left)
        q.push(self.root.right)

        while not q.empty():
            next_node = q.pop()
            if next_node.data == key:
                return next_node
            if next_node.left:
                q.push(next_node.left)
            if next_node.right:
                q.push(next_node.right)

        return None

    def dfs(self, key):
        """
        Depth-first search for the matching key.

        :param key: Key to check for data in a node being searched for.
        :return: The TreeNode containing the key, else None.
        """
        s = Stack()
        s.push(self.root.left)
        s.push(self.root.right)

        while not s.empty():
            next_node = s.pop()
            if next_node.data == key:
                return next_node
            if next_node.left:
                s.push(next_node.left)
            if next_node.right:
                s.push(next_node.right)

        return None

    def size(self):
        """
        Returns the number of nodes in the tree.
        :return: The number of nodes in the tree.
        """
        return len(self.traverse_inorder())
