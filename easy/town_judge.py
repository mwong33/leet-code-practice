class Solution:
    # O(E + V) Time, O(V) space
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            if N == 1:
                return 1
            else:
                return -1
        
        trust_dict = {}
        
        for rel in trust:
            # Deem the person with trust as True
            if rel[0] not in trust_dict:
                trust_dict[rel[0]] = (True, 0)
            else:
                trust_dict[rel[0]] = (True, trust_dict[rel[0]][1])
                
            if rel[1] not in trust_dict:
                trust_dict[rel[1]] = (False, 1)
            else:
                trust_dict[rel[1]] = (trust_dict[rel[1]][0], trust_dict[rel[1]][1] + 1)
        
        print(trust_dict)
        
        for person, data in trust_dict.items():
            if data[0] == False and data[1] == N - 1:
                return person
    
        return -1
    
"""
{Person: (Trusts, Trust Count)}
"""
