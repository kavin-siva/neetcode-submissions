class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
            
        ROWS, COLS = len(matrix), len(matrix[0])
        
        # Virtual 1D array boundaries
        low = 0
        high = (ROWS * COLS) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Map the 1D index back to 2D coordinates (row, col)
            row = mid // COLS
            col = mid % COLS
            
            mid_val = matrix[row][col]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                low = mid + 1   # Target is in the right half
            else:
                high = mid - 1  # Target is in the left half
                
        return False

        