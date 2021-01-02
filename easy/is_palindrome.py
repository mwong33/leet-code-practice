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
    
    # O(n) time O(1) space
    def isPalindromeSetSolution(self, s: str) -> bool:
        if len(s) == 0:
            return True
        
        start = 0
        end = len(s) - 1
        the_set = {"0","1","2","3","4","5","6","7","8","9",
                   "a","b","c","d","e","f","g","h","i","j",
                   "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"}
        
        while start <= end:
            start_char = s[start].lower()
            end_char = s[end].lower()
            
            if start_char not in the_set:
                start += 1
            elif end_char not in the_set:
                end -= 1
            else:
                if start_char != end_char:
                    return False
                start += 1
                end -= 1
                
        return True
