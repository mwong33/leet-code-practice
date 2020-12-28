class Solution:
    # O(n^2) time O(1) space
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s[0]
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            length_1 = self.middleOut(s, i, i)
            length_2 = self.middleOut(s, i, i+1)
            max_length = max(length_1, length_2)
            
            if max_length > (end - start + 1):
                start = i - ((max_length-1)//2)
                end = i + (max_length//2)
                
        return s[start:end+1]
        
    def middleOut(self, s, start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1

        return end - start - 1
