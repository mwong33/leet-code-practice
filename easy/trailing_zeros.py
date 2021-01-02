class Solution:
    # O(n + logm) O(1) space where n is the input n and m is n!
    def trailingZeroes(self, n: int) -> int:
        # Get that actual factorial value
        if n == 0 or n == 1 or n == 2:
            return 0
                    
        index = 3
        factorial = 2
        
        while index <= n:
            factorial = factorial * index
            index += 1
                    
        # Start dividing by 10
        zero_count = 0
        
        while factorial >= 10:
            if factorial % 10 != 0:
                break
            
            factorial = factorial // 10
            zero_count += 1
            
        return zero_count
