class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        path = []
        # Use a hash set for O(1) lookups to track which elements are in the current path
        used = set()
        
        def backtrack():
            # Base Case: If the path length matches the input length, we found a complete permutation
            if len(path) == len(nums):
                res.append(path.copy()) # Append a copy since 'path' is modified in-place
                return
            
            for num in nums:
                if num in used:
                    continue
                
                # 1. Choose: Add the number to our current path
                path.append(num)
                used.add(num)
                
                # 2. Explore: Recurse to find the next elements
                backtrack()
                
                # 3. Unchoose: Backtrack by removing the element before trying the next branch
                path.pop()
                used.remove(num)
                
        backtrack()
        return res

        