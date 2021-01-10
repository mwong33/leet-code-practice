class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert our wordDict into a set
        wordSet = set()
        
        for word in wordDict:
            wordSet.add(word)
            
        return self.wordBreakMemo(s, wordSet, {})
    
    def wordBreakMemo(self, s, wordSet, cache):
        # Starting with the first character, see if there are any words in our set
        # that match it and loop until we reach end of the word
        if s in wordSet:
            return True
        
        if s in cache:
            return cache[s]
        
        spawn_array = []
        
        for index in range(1, len(s)+1):
            if s[0:index] in wordSet:
                spawn_array.append(s[index:])
                
        for spawn in spawn_array:
            if spawn not in cache:
                result = self.wordBreakMemo(spawn, wordSet, cache)
                cache[spawn] = result
                if result:
                    return True
            elif cache[spawn]:
                return True
            
        return False
        
"""

"cats"
["c", "ats"] -> True

"cats"

["ca", "ts"] -> True

        "cats"
        /      \
    "c" "ats"  "ca" "ts" 
        /    \
     "a" "ts" "at" "s"
     
["c", "ca", "ts"]
