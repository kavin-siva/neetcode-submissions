from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()  # Stores indices of elements
        res = []
        
        for i, num in enumerate(nums):
            # 1. Remove indices that are out of the current window's bounds
            if q and q[0] < i - k + 1:
                q.popleft()
                
            # 2. Maintain monotonic decreasing property: 
            # Remove smaller elements from the back since they can't be the maximum anymore
            while q and nums[q[-1]] < num:
                q.pop()
                
            # 3. Add current element's index to the back of the queue
            q.append(i)
            
            # 4. If the window has hit size k, append the maximum to our result
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res

        