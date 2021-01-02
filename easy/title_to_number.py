class Solution:
    # O(n) time O(1) space
    def titleToNumber(self, s: str) -> int:
        # ord - 64
        
        num = 0
        
        for i in range(len(s) - 1, -1, -1):
            char_num = ord(s[i]) - 64
            
            if i == len(s) - 1:
                num += char_num
            else:
                num += (char_num * (26 ** (len(s) - 1 - i)))
            
        return num
