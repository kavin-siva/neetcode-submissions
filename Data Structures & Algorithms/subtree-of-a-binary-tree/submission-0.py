class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        # If the main tree is empty, subRoot cannot be a subtree of it
        if not root:
            return False
        
        # Check if the tree rooted at the current node matches subRoot exactly
        if self.isSameTree(root, subRoot):
            return True
            
        # Otherwise, check if subRoot matches any subtree in the left or right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # If both nodes are null, they are structurally identical
        if not p and not q:
            return True
        # If only one node is null or their values don't match, they aren't identical
        if not p or not q or p.val != q.val:
            return False
            
        # Structurally verify both the left and right subtrees recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        