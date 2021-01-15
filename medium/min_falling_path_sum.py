class Solution:
    # Top Down Memo - O(m*n) time O(m*n) space
    def minFallingPathSum(self, A: List[List[int]]) -> int:
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
