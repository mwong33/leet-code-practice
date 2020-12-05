class Solution:
    # O(n*m) space O(n*mlogm) where n is the number of words and m is the average     
    # word length
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        grouped_anagrams = []
        
        for word in strs:
            sorted_word_list = sorted(word)
            sorted_word = "".join(sorted_word_list)
            if sorted_word not in sorted_words.keys():
                sorted_words[sorted_word] = [word]
            else:
                sorted_words[sorted_word].append(word)
                
        for key in sorted_words.keys():
            grouped_anagrams.append(sorted_words[key])
                
        return grouped_anagrams
