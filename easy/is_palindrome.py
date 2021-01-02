class Solution:
    # O(n) time O(1) space
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        start = 0
        end = len(s) - 1
        
        while start <= end:
            start_char = s[start].lower()
            end_char = s[end].lower()
            
            if (ord(start_char) < 48 or ord(start_char) > 122 or (ord(start_char) > 57 and ord(start_char) < 97)):
                start += 1
            elif (ord(end_char) < 48 or ord(end_char) > 122 or (ord(end_char) > 57 and ord(end_char) < 97)):
                end -= 1
            else:
                if start_char != end_char:
                    return False
                start += 1
                end -= 1
                
        return True
