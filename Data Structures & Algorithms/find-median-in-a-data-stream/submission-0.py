import heapq

class MedianFinder:

    def __init__(self):
        # max-heap to store the smaller half of numbers. 
        # Python only has min-heaps, so we store negative values to simulate a max-heap.
        self.small = [] 
        # min-heap to store the larger half of numbers.
        self.large = [] 

    def addNum(self, num: int) -> None:
        # 1. Add to max-heap 'small' first (negated)
        heapq.heappush(self.small, -num)
        
        # 2. Correctness check: Ensure every element in 'small' is <= every element in 'large'
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # 3. Balance sizes: Ensure sizes don't differ by more than 1 element
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        # If one heap has more elements, the median is its root
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        if len(self.large) > len(self.small):
            return float(self.large[0])
            
        # If heaps are of equal size, the median is the average of both roots
        return (-self.small[0] + self.large[0]) / 2.0

        
        