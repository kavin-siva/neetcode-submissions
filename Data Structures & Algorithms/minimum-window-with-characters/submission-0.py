from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        # Dictionary to keep track of all the unique characters needed in t
        dict_t = Counter(t)
        required = len(dict_t)
        
        # Dictionary to keep track of unique characters in the current window
        window_counts = {}
        
        # formed keeps track of how many unique characters in t have met their frequency requirement in the current window
        formed = 0
        
        # Ans tuple: (window length, left, right)
        ans = (float("inf"), None, None)
        
        left = 0
        for right, char in enumerate(s):
            # Add character from the right to the window
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the frequency of the current character matches its required frequency in t
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Try and contract the window till the point it ceases to be 'valid'
            while left <= right and formed == required:
                left_char = s[left]
                
                # Save the smallest window details so far
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # The character at the position pointed by the `left` pointer is no longer a part of the window
                window_counts[left_char] -= 1
                if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                    formed -= 1
                
                # Move the left pointer ahead to look for a new window
                left += 1    
        
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

        