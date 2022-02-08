# A problem where you need to find the number of paths inside a tree where
# the sum of all nodes inside the path equals the target

# example:
# input tree:
#           5
#          / \
#        4    8
#       /   /   \
#      11   13  4
#     /\        /\
#    7  2      5  1
# target: 22
# result: 3
# explaination:
# the sum of the paths [5, 4, 11, 2], [4, 11, 7], [5, 8, 4, 5] equals 22

from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def path_sum(root: TreeNode, target: int, running_sum: int=None, memo: defaultdict=None) -> int:
    # time complexity: O(n)
    if root is None:
        return 0
    
    if memo is None:
        memo = defaultdict(int)
        memo[0] = 1
    if running_sum is None:
        running_sum = 0

    running_sum += root.val
    count = memo.get(running_sum-target, 0)
    memo[running_sum] += 1

    count += path_sum(root.left, target, running_sum, memo) \
        + path_sum(root.right, target, running_sum, memo)

    memo[running_sum] -= 1

    return count


if __name__ == "__main__":
    # TESTS:
    tree = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    tree2 = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))

    print(path_sum(tree, 22))  # 3
    print(path_sum(tree2, 8))  # 3