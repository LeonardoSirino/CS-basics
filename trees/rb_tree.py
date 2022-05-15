from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TreeNode:
    value: int
    parent: Optional[TreeNode] = None
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None
    black_: bool = field(default=False, init=False)

    def get_sibling(self) -> Optional[TreeNode]:
        if self.parent is None:
            return None

        if self.parent.left is self:
            return self.parent.right
        else:
            return self.parent.left


@dataclass
class Tree:
    root: Optional[TreeNode] = None

    def add_node(self, node: TreeNode) -> None:
        if self.root is None:
            self.root = node
            self.root.black_ = True

            return

        # NOTE performing the normal insertion in a tree
        curr = self.root
        previous = self.root
        while curr is not None:
            previous = curr
            if node.value >= curr.value:
                curr = curr.right
            else:
                curr = curr.left

        node.parent = previous
        if node.value >= previous.value:
            previous.right = node
        else:
            previous.left = node

        self._check_balance(node)

    def _check_balance(self, node: TreeNode) -> None:
        if node.parent is None or node.parent.black_:
            return

        uncle = node.parent.get_sibling()

        if uncle is not None and not uncle.black_:
            node.parent.black_ = True
            uncle.black_ = True

            node.parent.parent.black_ = False
            self._check_balance(node.parent.parent)


def main():
    tree = Tree()

    for i in range(5):
        node = TreeNode(value=i)
        tree.add_node(node)

    print(tree)


if __name__ == '__main__':
    main()
