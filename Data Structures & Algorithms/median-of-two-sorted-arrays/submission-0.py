class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        # Ensure A is the smaller array to minimize binary search range O(log(min(M,N)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            # i is the middle cut pointer for array A
            i = (l + r) // 2
            # j is the calculated cut pointer for array B to ensure total left elements == half
            j = half - i - 2
            
            # Handle boundary conditions when partition indices fall out of array bounds
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements: median is the smallest element of the right half
                if total % 2:
                    return min(Aright, Bright)
                # Even total elements: average of max(left) and min(right)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                # Cut in A is too far right; move it left
                r = i - 1
            else:
                # Cut in A is too far left; move it right
                l = i + 1

        