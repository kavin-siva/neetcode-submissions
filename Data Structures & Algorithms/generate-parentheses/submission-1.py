class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        stack = []
        
        def backtrack(open_count, closed_count):
            # Base Case: Valid combination completed
            if open_count == closed_count == n:
                res.append("".join(stack))
                return
            
            # Constraint 1: You can always add an open parenthesis if you have some left
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, closed_count)
                stack.pop() # Backtrack
                
            # Constraint 2: You can only add a closed parenthesis if it matches an open one
            if closed_count < open_count:
                stack.append(")")
                backtrack(open_count, closed_count + 1)
                stack.pop() # Backtrack
                
        backtrack(0, 0)
        return res

        