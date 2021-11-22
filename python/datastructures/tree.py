from __future__ import annotations


class Tree:
    def __init__(self, val: int, left: Tree=None, right: Tree=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        curr = self
        result = [curr.val]
        stack = []

        if self.left and self.right:
            stack = [curr.left, curr.right]

        while stack:
            curr = stack.pop(0)
            result.append(curr.val)

            if curr.left is not None:
                stack.extend([curr.left, curr.right])

        return str(result)

    def _invert(self, tree: Tree) -> Tree:
        if tree is None:
            return tree
        
        self._invert(tree.left)
        self._invert(tree.right)

        tree.left, tree.right = tree.right, tree.left

        return tree

    def invert(self) -> Tree:
        self = self._invert(self)
        
        return self





if __name__ == "__main__":
    # tests
    
    tree = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(7, Tree(6), Tree(9)))
    #       4
    #      / \
    #     2   7
    #    / \  /\
    #   1  3  6 9

    print(tree)
    tree.invert()
    print(tree)
    tree2 = Tree(1, Tree(2, tree, tree), Tree(3, tree, tree))
    #               1
    #              / \
    #             2   3
    #            /\   /\
    #           4 .. .. ..
    #          / \
    #         2   7
    #       / \  / \
    #      1  3  6  9


    print(tree2)
    tree2.invert()
    print(tree2)