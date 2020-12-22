class Solution:
    # O(n) time O(1) space
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3
        
        initial_minus_2 = 2
        initial_minus_1 = 3
        
        output = 0
        
        for i in range(4, n+1):
            output = initial_minus_1 + initial_minus_2
            initial_minus_2 = initial_minus_1
            initial_minus_1 = output
            
        return output
