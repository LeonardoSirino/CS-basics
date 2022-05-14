from __future__ import annotations

from dataclasses import dataclass
from operator import le
from typing import Any, List, Optional

from collections import deque


@dataclass
class Node:
    value: str
    left: Optional[Node] = None
    right: Optional[Node] = None


def create_tree() -> Node:
    A = Node('A')
    B = Node('B')
    C = Node('C')
    D = Node('D')
    E = Node('E')
    F = Node('F')
    G = Node('G')
    H = Node('H')
    I = Node('I')

    I.left = H
    G.right = I
    F.right = G

    D.left = C
    D.right = E

    B.left = A
    B.right = D

    F.left = B

    root = F

    return root


def pre_order(root: Node) -> str:
    stack = deque([root])
    values = ''

    while stack:
        node = stack.pop()
        values += node.value

        if not node.right is None:
            stack.append(node.right)

        if not node.left is None:
            stack.append(node.left)

    return values


def in_order(root: Node) -> str:
    """This method return the values in ascending order for a binary search tree

    Args:
        root (Node): root node of the tree

    Returns:
        str: list of values for in_order traversal
    """
    values = ''
    stack = deque([root])
    seen = set()

    while stack:
        node = stack.pop()
        if node.left is None or node.left.value in seen:
            seen.add(node.value)
            values += node.value

            if not node.right is None:
                stack.append(node.right)

        else:
            stack.append(node)
            stack.append(node.left)

    return values


def post_order(root: Node) -> str:
    """In this order the left subtree is returned first, then the right subtree and at last the
    root node value is returned.

    Args:
        root (Node): root node of the tree

    Returns:
        str: list of values for post_order traversal
    """
    values = ''
    stack = deque([root])
    seen = set()

    while stack:
        node = stack.pop()

        l_cond = node.left is None or node.left.value in seen
        r_cond = node.right is None or node.right.value in seen

        if l_cond and r_cond:
            seen.add(node.value)
            values += node.value
        else:
            stack.append(node)

            if not node.right is None:
                stack.append(node.right)

            if not node.left is None:
                stack.append(node.left)

    return values
