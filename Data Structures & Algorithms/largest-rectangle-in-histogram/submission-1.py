class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []  # Stores pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # If the current height is smaller than the height at the top of the stack,
            # it means we found the right boundary for the bar on top of the stack.
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # Calculate the width using the current index as the right boundary
                width = i - idx
                max_area = max(max_area, height * width)
                # The popped bar's starting index extends back to the current position
                start = idx
                
            stack.append((start, h))
            
        # Clear out any remaining elements in the stack
        # These bars extend all the way to the end of the histogram
        for idx, height in stack:
            width = len(heights) - idx
            max_area = max(max_area, height * width)
            
        return max_area

        