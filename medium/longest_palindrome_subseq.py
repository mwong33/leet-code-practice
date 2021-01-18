class Solution:
    # Top Down Memo O(s^2) time O(s^2) space
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.longestPalindromeSubseqMemo(s, 0, len(s)-1, {})
    
    def longestPalindromeSubseqMemo(self, text, start, end, cache):
        if (start, end) in cache:
            return cache[(start, end)]
        
        # 1 Character Case
        if start == end:
            return 1
        
        # Edge Case
        if start > end:
            return 0
        
        # Multiple Characters Case
        if text[start] == text[end]:
            cache[(start, end)] = 2 + self.longestPalindromeSubseqMemo(text, start+1, end-1, cache)
            return cache[(start, end)]
        else:
            cache[(start, end)] = max(self.longestPalindromeSubseqMemo(text, start+1, end, cache), self.longestPalindromeSubseqMemo(text, start, end-1, cache))
            return cache[(start, end)]
