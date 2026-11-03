class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # Calculate the midpoint
            # (l + r) // 2 is standard, but l + (r - l) // 2 prevents overflow in other languages
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1   # Target is in the right half
            else:
                r = mid - 1   # Target is in the left half
                
        return -1  # Target not found

        