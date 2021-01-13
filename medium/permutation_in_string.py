class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create an alphabet array for s1
        s1_array = self.getAlphabetArray(s1)
        
        # Loop through the s2 string with a window of size len(s1) and check if its
        # alphabet array is the same as that of s1's
        for start in range(0, len(s2) - len(s1) + 1):
            if self.getAlphabetArray(s2[start:start + len(s1)]) == s1_array:
                return True 
            
        return False
        
    def getAlphabetArray(self, a_string):
        alphabet_array = [0] * 26
        
        for character in a_string:
            alphabet_array[ord(character)-97] += 1
        
        return alphabet_array
