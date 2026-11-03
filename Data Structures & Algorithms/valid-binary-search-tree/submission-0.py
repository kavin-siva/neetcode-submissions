class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        stack = []
        curr = root
        prev = float('-inf')
        
        while curr or stack:
            # Traverse to the leftmost node
            while curr:
                stack.append(curr)
                curr = curr.left
                
            curr = stack.pop()
            
            # If the current value is not strictly greater than the previous, it's invalid
            if curr.val <= prev:
                return False
            prev = curr.val
            
            curr = curr.right
            
        return True

        