class Solution:
    # O(m) space O(n*m) time where n is the number of words and m is the longest prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 or len(strs[0]) == 0:
            return ""
        
        common_prefix = ""
        letter_index = 0
        keep_checking = True
        
        while keep_checking:
            if letter_index >= len(strs[0]):
                break
            
            candidate_letter = strs[0][letter_index]
            
            for word in strs:
                if letter_index >= len(word) or word[letter_index] != candidate_letter:
                    keep_checking = False
                    break
            
            if keep_checking:
                common_prefix += candidate_letter
                letter_index += 1
        
        return common_prefix
