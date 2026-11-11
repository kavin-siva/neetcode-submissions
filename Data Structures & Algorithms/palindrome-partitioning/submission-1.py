class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        part = []
        
        def dfs(i):
            # Base case: if we've reached the end of the string, record the partition
            if i >= len(s):
                res.append(part.copy())
                return
            
            # Explore all possible substrings starting from index i
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1]) # Choose
                    dfs(j + 1)            # Explore
                    part.pop()            # Unchoose (Backtrack)
                    
        dfs(0)
        return res

    def isPalindrome(self, s: str, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

        