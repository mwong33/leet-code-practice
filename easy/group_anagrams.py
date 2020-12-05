class Solution:
    # O(n*m) space O(n*mlogm) where n is the number of words and m is the average     
    # word length
    def groupAnagramsBySorting(self, strs: List[str]) -> List[List[str]]:
        sorted_words = {}
        
        for word in strs:
            sorted_word_tuple = tuple(sorted(word))
            if sorted_word_tuple not in sorted_words.keys():
                sorted_words[sorted_word_tuple] = [word]
            else:
                sorted_words[sorted_word_tuple].append(word)
                
        return sorted_words.values()
    
    # O(n*m) space O(n*m) where n is the number of words and m is the average     
    # word length
    def groupAnagramsByCount(self, strs: List[str]) -> List[List[str]]:
        anagrams_by_count = {}
        
        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter)-97] += 1
            if tuple(count) not in anagrams_by_count.keys():
                anagrams_by_count[tuple(count)] = [word]
            else:
                anagrams_by_count[tuple(count)].append(word)
                
        return anagrams_by_count.values()
