class Solution:
    # O(t) time and O(1) space where t is the length of array t
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        
        # Start with the first character of s
        # Iterate throug each character of t
        # If s is found in t, set to look for the next character in s. If s has no more characters, return true
        # return false if the loop is completed without returning true
        
        current_char_index = 0
        
        for char in t:
            if char == s[current_char_index]:
                current_char_index += 1
                if current_char_index == len(s):
                    return True
            
        return False
