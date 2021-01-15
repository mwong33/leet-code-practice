class Solution:
    # Top Down Memo - O(m*n) time O(m*n) space
    def minFallingPathSumTopDown(self, A: List[List[int]]) -> int:
        min_sum = None
        
        for index in range(len(A[0])):
            potential_sum = self.minFallingPathSumMemo(A, 0, index, {})
            if min_sum == None or min_sum > potential_sum:
                min_sum = potential_sum
        
        return min_sum
    
    def minFallingPathSumMemo(self, A, row, col, cache):
        if (row, col) in cache:
            return cache[(row, col)]
        
        # Base Case (Last Row)
        if row == len(A) - 1:
            return A[row][col]
        
        # Single Col Edge Case
        if col == 0 and col == len(A[0]) - 1:
            result = A[row][col] + self.minFallingPathSumMemo(A, row+1, col)
        # First Col Edge Case
        elif col == 0:
            result = A[row][col] + min(self.minFallingPathSumMemo(A, row+1, col, cache), self.minFallingPathSumMemo(A, row+1, col+1, cache))
        # Last Col Edge Case
        elif col == len(A[0]) - 1:
            result = A[row][col] + min(self.minFallingPathSumMemo(A, row+1, col, cache), self.minFallingPathSumMemo(A, row+1, col-1, cache))
        else:
            result = A[row][col] + min(self.minFallingPathSumMemo(A, row+1, col-1, cache), self.minFallingPathSumMemo(A, row+1, col, cache), self.minFallingPathSumMemo(A, row+1, col+1, cache))
        
        cache[(row, col)] = result
        
        return result

    # Bottom Up Table - O(m*n) time O(m*n) space
    def minFallingPathSumBottomUp(self, A: List[List[int]]) -> int:        
        # Start with the penultimate row
        # Work your way to the top row, choosing your minimum choices along the way
        # Return the min of the top row
        for row in range(len(A)-2, -1, -1):
            for col in range(len(A[0])):
                # Single Col Edge Case
                if col == 0 and col == len(A[0]) - 1:
                    A[row][col] += A[row+1][col] 
                # First Col Edge Case
                elif col == 0:
                    A[row][col] += min(A[row+1][col+1], A[row+1][col])
                # Last Col Edge Case
                elif col == len(A[0]) - 1:
                    A[row][col] += min(A[row+1][col-1], A[row+1][col])
                else:
                    A[row][col] += min(A[row+1][col-1], A[row+1][col], A[row+1][col+1])
   
        return min(A[0])
"""
Bottom Up

1  2  3  12 13 15
4  5  6  11 12 14
7  8  9  7  8  9
"""
