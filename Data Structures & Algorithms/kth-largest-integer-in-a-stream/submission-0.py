import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        
        # Trim the heap so it only retains the k largest elements seen so far
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # Push the new value onto the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap exceeds size k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of our min-heap is the k-th largest element overall
        return self.min_heap[0]

        
