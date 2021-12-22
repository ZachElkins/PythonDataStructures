import pytest
from data_structures.tree_node import TreeNode


@pytest.fixture
def head_node():
    return TreeNode(1)


def test_tree_node_init():
    node = TreeNode(1)


def test_tree_node_init_error():
    with pytest.raises(TypeError):
        node = TreeNode()


def test_tree_node_left(head_node):
    left_node = TreeNode(2)
    head_node.left = left_node
    assert head_node.left == left_node


def test_tree_node_left_error(head_node):
    with pytest.raises(TypeError):
        head_node.left = 2


def test_tree_node_right(head_node):
    right_node = TreeNode(2)
    head_node.right = right_node
    assert head_node.right == right_node


def test_tree_node_right_error(head_node):
    with pytest.raises(TypeError):
        head_node.right = 1


def test_tree_node_eq_error(head_node):
    with pytest.raises(TypeError):
        assert head_node == 1


def test_tree_node_lt(head_node):
    less_node = TreeNode(0)
    more_node = TreeNode(2)
    assert less_node < head_node
    assert not more_node < head_node


def test_tree_node_lt_error(head_node):
    with pytest.raises(TypeError):
        assert head_node < 1


def test_tree_node_le(head_node):
    less_node = TreeNode(1)
    more_node = TreeNode(2)
    assert less_node <= head_node
    assert not more_node <= head_node


def test_tree_node_le_error(head_node):
    with pytest.raises(TypeError):
        assert head_node <= 1


def test_tree_node_gt(head_node):
    less_node = TreeNode(0)
    more_node = TreeNode(1)
    assert more_node >= head_node
    assert not less_node >= head_node


def test_tree_node_gt_error(head_node):
    with pytest.raises(TypeError):
        assert head_node > 0


def test_tree_node_ge(head_node):
    less_node = TreeNode(0)
    more_node = TreeNode(2)
    assert more_node > head_node
    assert not less_node > head_node


def test_tree_node_ge_error(head_node):
    with pytest.raises(TypeError):
        assert head_node >= 0


