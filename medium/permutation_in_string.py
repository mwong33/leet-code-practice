class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Create an alphabet array for s1
        s1_dict = self.getAlphabetDict(s1)
        
        # Loop through the s2 string with a window of size len(s1) and check if its
        # alphabet array is the same as that of s1's
        for start in range(0, len(s2) - len(s1) + 1):
            if self.getAlphabetDict(s2[start:start + len(s1)]) == s1_dict:
                return True 
            
        return False
        
    def getAlphabetDict(self, a_string):
        a_dict = {}
        
        for char in a_string:
            if char in a_dict:
                a_dict[char] += 1
            else:
                a_dict[char] = 1
        
        return a_dict
