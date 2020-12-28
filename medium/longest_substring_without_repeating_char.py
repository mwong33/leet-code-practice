import queue

class Solution:
    # O(n) time O(n) space
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Keep a set to keep track of the letters in our current substring
        # Keep a rolling integer to keep track of our longest substring with unique letters
        # Keep track of two indexes for our rolling window
        
        if len(s) == 0:
            return 0
        
        substring_set = set()
        max_length = 0       
        start = 0
        end = 0
        
        while end < len(s):
            if s[end] not in substring_set:
                substring_set.add(s[end])
                end += 1
            else:
                substring_set.remove(s[start])
                start += 1
            
            if len(substring_set) > max_length:
                max_length = len(substring_set)
                
        return max_length
