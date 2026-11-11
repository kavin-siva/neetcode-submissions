# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Base case: Both nodes are None (reached the end of identical paths)
        if not p and not q:
            return True
        
        # One node is None or the values don't match (structural mismatch)
        if not p or not q or p.val != q.val:
            return False
            
        # Recursively check the left subtrees and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        