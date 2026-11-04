class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                
                # Create unique identifiers for row, column, and 3x3 sub-box
                row_key = f"row {i} {val}"
                col_key = f"col {j} {val}"
                box_key = f"box {i // 3} {j // 3} {val}"
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
                
        return True

        