from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Maps key -> list of [timestamp, value] pairs
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        if not values:
            return ""
        
        left, right = 0, len(values) - 1
        result = ""
        
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                # Valid candidate; record it and search right for a closer timestamp
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
                
        return result

        
