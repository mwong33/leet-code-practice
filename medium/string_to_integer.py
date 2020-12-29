import math

class Solution:
    # O(n) time O(1) space
    def myAtoi(self, s: str) -> int:
        # Get rid of white space
        s = s.strip()
        
        if len(s) == 0: 
            return 0
        if s[0] not in "+-1234567890": 
            return 0
        
        number_start = 0        
        if s[0] == "-" or s[0] == "+":
            if len(s) == 1:
                return 0
            
            number_start = 1            
            if s[number_start] not in "1234567890":
                return 0
            
        number_end =  number_start       
        while number_end < len(s):
            if s[number_end] not in "1234567890":
                break
            number_end += 1
        
        number = int(s[number_start:number_end])
        
        if s[0] == "-":
            number = number * -1
            
        if number > math.pow(2,31) - 1:
            return int(math.pow(2,31) - 1)
        
        if number < math.pow(2,31) * -1:
            return int(math.pow(2,31) * -1)
        
        return number
