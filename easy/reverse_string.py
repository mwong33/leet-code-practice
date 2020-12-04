class Solution:
    # O(1) space O(n) time
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        first_char_index = 0
        last_char_index = len(s) - 1
        
        while first_char_index < last_char_index:
            temp_char = s[first_char_index]
            s[first_char_index] = s[last_char_index]
            s[last_char_index] = temp_char
            
            first_char_index += 1
            last_char_index -= 1
