class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # O(letter_count) where letter_count is number of words we store 
        # At worst case no words have common prefixes and we store each character
        # of each word individually
        self.trie = {}
        
    # O(n) time O(n) space where n is the number of letters in the word
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        current_dict = self.trie
        
        for ch in word:
            if ch not in current_dict:
                current_dict[ch] = {}
            current_dict = current_dict[ch]

        current_dict["*"] = True
    
    # O(n) time O(1) space where n is the number of letters in the word
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        current_dict = self.trie
        
        for ch in word:
            if ch not in current_dict:
                return False
            current_dict = current_dict[ch]
            
        if "*" not in current_dict:
            return False
        
        return True
    
    # O(n) time O(1) space where n is the number of letters in the prefix
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        current_dict = self.trie
        
        for ch in prefix:
            if ch not in current_dict:
                return False
            current_dict = current_dict[ch]
                    
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
