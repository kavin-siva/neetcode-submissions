# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_diameter
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            # Longest path passing through the current node
            max_diameter = max(max_diameter, left_height + right_height)

            # Height of the subtree rooted at the current node
            return 1 + max(left_height, right_height)

        dfs(root)
        return max_diameter

        