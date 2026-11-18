class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            hours_needed = sum((pile + mid - 1) // mid for pile in piles)

            if hours_needed <= h:
                # mid is fast enough; try to find an even slower valid speed
                right = mid
            else:
                # mid is too slow; need a strictly faster speed
                left = mid + 1

        return left

        