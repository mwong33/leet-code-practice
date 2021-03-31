class Solution:
    # O(glogg + slogs) time O(1) space where s is the length of the s array.
    # and g is the length of the g array.
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0:
            return 0
        
        g.sort()
        s.sort()
        
        # 1) Pop the end of array g
        # 2) Compare it with the end of s
        # 3) If g is <= s, pop s. Increment satisfied_child by 1
        
        satisfied_child = 0
        
        for i in range(len(g)):
            last_child = g.pop()
            
            if len(s) > 0 and last_child <= s[len(s) - 1]:
                satisfied_child += 1
                s.pop()
                
            if len(s) == 0:
                break
                
        return satisfied_child
