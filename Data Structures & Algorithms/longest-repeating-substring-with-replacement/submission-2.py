class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_len = 0
        max_freq = 0  # Tracks the highest frequency of any single character seen so far
        
        left = 0
        for right in range(len(s)):
            # Add the incoming character to our frequency map
            count[s[right]] = count.get(s[right], 0) + 1
            
            # Maintain the maximum frequency of any character in the current window
            max_freq = max(max_freq, count[s[right]])
            
            # Current window length is (right - left + 1)
            # If remaining characters to replace exceed k, shrink the window from the left
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                # Note: We do not strictly need to decrement max_freq here. 
                # A smaller max_freq would never yield a larger max_len than what we've already found.
            
            # Capture the maximum valid window size found
            max_len = max(max_len, right - left + 1)
            
        return max_len

        