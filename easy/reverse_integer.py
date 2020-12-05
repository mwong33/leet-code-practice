class Solution:
    # O(1) space and O(n) time where n is the number of digits
    def reverse(self, x: int) -> int:        
        abs_x = abs(x)
        
        rev = 0
        
        while abs_x > 0:
            last_digit = abs_x%10
            rev = rev * 10 + last_digit
            abs_x = abs_x//10
    
        if rev > 2**31 - 1 or rev < -1 * 2**31:
            return 0
            
        return rev if x > 0 else -1 * rev
