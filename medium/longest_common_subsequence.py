class Solution:
    # Top Down Memo - O(text1*text2) time O(text1*text2) space
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.longestCommonSubsequenceMemo(text1, text2, len(text1)-1, len(text2)-1, {})
    
    def longestCommonSubsequenceMemo(self, text1, text2, index1, index2, cache):
        if (index1, index2) in cache:
            return cache[(index1, index2)]     
        
        if index1 == -1 or index2 == -1:
            return 0
        
        # Given the last character is the same
        if text1[index1] == text2[index2]:
            result = 1 + self.longestCommonSubsequenceMemo(text1, text2, index1-1, index2-1, cache)
            cache[(index1, index2)] = result
            return result
        
        # Given the last characters are different
        result = max(self.longestCommonSubsequenceMemo(text1, text2, index1-1, index2, cache), self.longestCommonSubsequenceMemo(text1, text2, index1, index2-1, cache))
        cache[(index1, index2)] = result
        return result
