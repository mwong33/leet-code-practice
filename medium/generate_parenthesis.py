class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def genParenthesisHelper(combo, left_count, right_count, n):
            if left_count + right_count == 2 * n:
                result.append(combo)
                return

            if left_count < n:
                genParenthesisHelper(combo+"(", left_count+1, right_count, n)
            if right_count < left_count:
                genParenthesisHelper(combo+")", left_count, right_count+1, n)
        
        genParenthesisHelper("", 0, 0, n)
        return result

"""
You can only have n left parentheses and n right parentheses

We can use backtrackign to generate call combinations

we start of by prioritizing generating all left parenthesis up to n

then we generate right up to the amount of left parenthesis we have

backtrack each time to generate combinations
"""
