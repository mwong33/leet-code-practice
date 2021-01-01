class Solution:
    # O(n*m) O(1) space naive solution
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_length = len(haystack)
        needle_length = len(needle)
        
        if needle_length == 0:
            return 0
        
        if needle_length > haystack_length:
            return -1
        
        for i in range(0, haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i
        return -1
