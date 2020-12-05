class Solution:
    # O(n*m) space O(n*mlogm) where n is the number of words and m is the average     
    # word length
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        
        for word in strs:
            sorted_word_tuple = tuple(sorted(word))
            if sorted_word_tuple not in sorted_words.keys():
                sorted_words[sorted_word_tuple] = [word]
            else:
                sorted_words[sorted_word_tuple].append(word)
                
        return sorted_words.values()
