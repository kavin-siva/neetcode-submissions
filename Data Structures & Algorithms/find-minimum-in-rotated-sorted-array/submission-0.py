from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # Minimum is at mid or in the left half
            else:
                right = mid
                
        return nums[left]

        