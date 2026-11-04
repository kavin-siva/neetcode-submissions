class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # Map values to their indices in inorder array for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0
        
        def helper(in_left, in_right):
            nonlocal pre_idx
            
            # Base case: no elements left to construct this subtree
            if in_left > in_right:
                return None
            
            # Select the current root value from preorder array
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1
            
            # Locate where this root splits the inorder array
            mid = inorder_map[root_val]
            
            # Recursively build the left and right subtrees.
            # IMPORTANT: Must build Left before Right because preorder processes left first.
            root.left = helper(in_left, mid - 1)
            root.right = helper(mid + 1, in_right)
            
            return root
            
        return helper(0, len(inorder) - 1)

        