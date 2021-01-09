# O(n) space O(n) time
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.numDecodingsMemo({}, s)
    
    def numDecodingsMemo(self, cache, s):
        # If we encounter a 0 length string return 0
        if len(s) == 0:
            return 0
        
        # See if we start with a 0
        if s[0] == "0":
            return 0
        
        # If the string is of length 1 return 1
        if len(s) == 1:
            return 1
         
        # Determine if the prefix is invalid
        if s[1] == "0" and int(s[:2]) > 26:
            return 0
        
        # If the string is of length 2 return either 1, 2
        if len(s) == 2:
            if int(s[:2]) > 26:
                return 1
            elif s[1] == "0":
                return 1
            else:
                return 2
        
        # Check how many sides we can extend to
        left_side = 0
        right_side = 0
        
        if int(s[:2]) > 26:
            if s[1:] not in cache:
                left_side = self.numDecodingsMemo(cache, s[1:])
                cache[s[1:]] = left_side
            else:
                left_side = cache[s[1:]]
            
        elif s[1] == "0":
            if s[2:] not in cache: 
                right_side = self.numDecodingsMemo(cache, s[2:])
                cache[s[2:]] = right_side
            else:
                right_side = cache[s[2:]]
        else:
            if s[1:] not in cache:
                left_side = self.numDecodingsMemo(cache, s[1:])
                cache[s[1:]] = left_side
            else:
                left_side = cache[s[1:]]
            if s[2:] not in cache: 
                right_side = self.numDecodingsMemo(cache, s[2:])
                cache[s[2:]] = right_side
            else:
                right_side = cache[s[2:]]
                
        return left_side + right_side
        
        
"""
Example 1:

            "1234"
        /         \
    "1" "234"      "12" "34"
        /    \            /
    "2" "34" "23" "4"    "3" "4"
         /       /           /  
      "3" "4"   "4"         "4"
          /
         "4"
        
Example 2:

            "1034"
                \
                "10" "34"   
                       /
                      "3" "4"
                            \
                            "4"
Example 3:      
            "3034"
            
0

Example 4:
    
        "1304"
        /
    "1" "304"
    
        
"""      
