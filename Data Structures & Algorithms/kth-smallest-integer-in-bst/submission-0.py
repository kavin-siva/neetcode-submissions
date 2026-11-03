class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        res = []
        
        def inorder(node):
            if not node or len(res) >= k:
                return
            
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
            
        inorder(root)
        return res[k - 1]

        