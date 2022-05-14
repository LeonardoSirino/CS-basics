from .tree_traversal import create_tree, in_order, post_order, pre_order


def test_pre_order():
    root = create_tree()

    values = pre_order(root)
    target = 'FBADCEGIH'

    assert values == target


def test_post_order():
    root = create_tree()

    values = post_order(root)
    target = 'ACEDBHIGF'

    assert values == target


def test_in_order():
    root = create_tree()

    values = in_order(root)
    target = 'ABCDEFGHI'

    assert values == target
