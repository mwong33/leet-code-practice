class Solution:
    # O(n*k) time O(n) space
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return "0"
        
        stack = []
        
        for digit in num:
            while k > 0 and len(stack) > 0 and int(digit) < stack[len(stack) - 1]:
                stack.pop()
                k = k - 1
            stack.append(int(digit))
                
        while k > 0:
            stack.pop()
            k = k - 1
        
        final_string = ""
        
        for digit in stack:
            final_string += str(digit)
            
        return str(int(final_string))
