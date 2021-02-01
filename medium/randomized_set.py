import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        
        position = len(self.array)
        self.dict[val] = position
        self.array.append(val)
        
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
            
        position = self.dict[val]
        
        if position != len(self.array) - 1:   
            last_element = self.array.pop()
            self.array[position] = last_element

            del self.dict[val]
            self.dict[last_element] = position
        else:
            self.array.pop()
            del self.dict[val]
        
        return True
        
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.array)
        
"""
HashMap

{1: 0, 2: 1, 3: 2}
[1,2,3]

Remove 2 - Grab the last element and move it into 2's position. 
           Update the HasMap Accordingly
           
{1:0, 3:1}
[1,3]

Get Random, use random to generate a randome int to index into our array

"""

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
