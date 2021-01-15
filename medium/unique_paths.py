class Solution:
    # Top Down Memo - O(m*n) time O(m*n) space
    def uniquePaths(self, m: int, n: int) -> int:
        return self.uniquePathsMemo(m, n, 1, 1, {})
    
    def uniquePathsMemo(self, m, n, row, col, cache):
        if (row, col) in cache:
            return cache[(row, col)]
        
        # Base Case
        if row == m and col == n:
            return 1
        
        # Last Row Edge Case
        if row == m:
            result = self.uniquePathsMemo(m, n, row, col+1, cache)
            cache[(row, col)] = result
            return result
        
        # Last Col Edge Case
        if col == n:
            result = self.uniquePathsMemo(m, n, row+1, col, cache)
            cache[(row, col)] = result
            return result
        
        result = self.uniquePathsMemo(m, n, row, col+1, cache) + self.uniquePathsMemo(m, n, row+1, col, cache)
        cache[(row, col)] = result
        return result
