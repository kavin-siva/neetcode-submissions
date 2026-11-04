class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # Initialize with negative infinity to handle trees with all negative values
        global_max = float('-inf')
        
        def dfs(node):
            nonlocal global_max
            if not node:
                return 0
            
            # Compute the max path sum from the left and right subtrees.
            # If a subtree returns a negative sum, we choose 0 (ignore it).
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            
            # Calculate the path sum if we decide to "split" at the current node
            # (i.e., using this node as the highest turning point of the path)
            current_split_sum = node.val + left_max + right_max
            
            # Update our global maximum if the split path is larger
            global_max = max(global_max, current_split_sum)
            
            # Return the maximum single branch sum to the parent node
            return node.val + max(left_max, right_max)
            
        dfs(root)
        return global_max

        