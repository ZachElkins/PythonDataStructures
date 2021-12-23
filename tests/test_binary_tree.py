import pytest
from data_structures.binary_tree import BinaryTree
from data_structures.tree_node import TreeNode


@pytest.fixture
def base_tree():
    tree = BinaryTree(28)
    tree.insert(14)
    tree.insert(56)
    tree.insert(112)
    tree.insert(7)
    return tree


def test_binary_tree_init_from_data():
    tree = BinaryTree(2)
    assert isinstance(tree, BinaryTree)


def test_binary_tree_init_from_tree_node():
    node = TreeNode(10)
    tree = BinaryTree(node)
    assert tree.root == node


def test_binary_tree_insert():
    tree = BinaryTree(2)
    tree.insert(1)
    tree.insert(3)
    assert tree.root.data == 2
    assert tree.root.left.data == 1
    assert tree.root.right.data == 3


def test_binary_tree_inorder_traversal(base_tree):
    assert base_tree.traverse_inorder() == [7, 14, 28, 56, 112]


def test_binary_tree_preorder_traversal(base_tree):
    assert base_tree.traverse_preorder() == [28, 14, 7, 56, 112]


def test_binary_tree_delete(base_tree):
    base_tree.delete(28)
    assert base_tree.root.data == 112
    assert base_tree.traverse_preorder() == [112, 14, 7, 56]


def test_binary_tree_delete_no_children():
    tree = BinaryTree(12)
    tree.insert(10)
    tree.insert(14)
    assert tree.traverse_inorder() == [10, 12, 14]
    tree.delete(10)
    assert tree.traverse_inorder() == [14, 12]
    tree.delete(14)
    assert tree.traverse_inorder() == [12]
    tree.delete(12)


def test_binary_tree_bfs(base_tree):
    assert base_tree.bfs(112).data == 112
    assert base_tree.bfs(111) is None


def test_binary_tree_dfs(base_tree):
    assert base_tree.dfs(112).data == 112
    assert base_tree.dfs(111) is None


def test_binary_tree_size(base_tree):
    assert base_tree.size() == 5
    base_tree.delete(112)
    assert base_tree.size() == 4
