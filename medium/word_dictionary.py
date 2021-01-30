class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # O(word_count) where word_count is number of words we store 
        # At worst case no words have common prefixes and we store each character
        # of each word individually
        self.trie = {}
    
    # O(n) time where n is the lenghth of the word. O(n) space
    def addWord(self, word: str) -> None:
        current_dict = self.trie
        
        for ch in word:
            if ch in current_dict:
                current_dict = current_dict[ch]
            else:
                current_dict[ch] = {}
                current_dict = current_dict[ch]
                
        current_dict["*"] = True 
                
    # O(m) time for well defined words and O(1) space
    # O(n*26^m) O(m) space for undefined words where n is the number of keys and 
    # m is the length of the word to search
    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.trie)
    
    def searchHelper(self, word, dictionary):
        current_dict = dictionary
        
        for index in range(len(word)):
            ch = word[index]
            if ch != ".":
                if ch not in current_dict:
                    return False
                else:
                    current_dict = current_dict[ch]
            else:                
                for option in current_dict.keys():
                    if option == "*":
                        continue
                    if self.searchHelper(word[index+1:], current_dict[option]):
                        return True
                    
                return False
         
        if "*" not in current_dict:
            return False
        
        return True
              
"""
"bad", "dad", "mad"

{
    "b": {
        "a": {
            "d": {
                "*": True
            }
        }
    }
    "d": {
        "a": {
            "d": {
                "*": True
            }    
        }
    }
    "m": {
        "a": {
            "d": {
                "*": True
            }
        }
    }
}


"""

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
