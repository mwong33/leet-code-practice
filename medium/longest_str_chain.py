# O(n^2) time O(n) space
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Convert our word list to a set
        word_set = set()
        
        for word in words:
            word_set.add(word)
            
        rolling_max = 0
        cache = {}
                
        for word in words:
            word_longest_chain = self.longestStrChainForWord(word_set, word, cache)
            if word_longest_chain > rolling_max:
                rolling_max = word_longest_chain
                
        return rolling_max
            
            
    def longestStrChainForWord(self, word_set, word, cache):
        # Split the word (remove one of each character and add it to our set)
        if word in cache:
            return cache[word]
        
        split_set = self.splitWord(word_set, word)
        
        longest_chain_sum = 1
        
        for split_word in split_set:
            if split_word in cache:
                if 1 + cache[split_word] > longest_chain_sum:
                    longest_chain_sum = 1 + cache[split_word]
            else:
                result = self.longestStrChainForWord(word_set, split_word, cache)
                cache[split_word] = result
                if 1 + result > longest_chain_sum:
                    longest_chain_sum = 1 + result
                    
        return longest_chain_sum
        
    # Helper function that splits a word and only returns a set of words that are in our word_set
    def splitWord(self, word_set, word):
        split_set = set()
        
        for i in range(len(word)):
            if word[:i] + word[i+1:] in word_set:
                split_set.add(word[:i] + word[i+1:])
                
        return split_set
        
"""
Top Down

                "xbc"                  
            "xb" , "xc", "bc"
        "x"   "b"  "x"  "c"   "b"  "c"
"""
