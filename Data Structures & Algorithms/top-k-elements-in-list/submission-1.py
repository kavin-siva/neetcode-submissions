from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        
        # Push elements onto a min-heap, maintaining a maximum size of k
        # We store tuples as (frequency, element)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        # Extract elements from the heap
        return [num for freq, num in heap]

        