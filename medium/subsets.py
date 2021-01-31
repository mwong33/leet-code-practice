class Solution:
    # O(n*2^n) time O(n*2^n) space
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for number in nums:
            addition = []
            for old in output:
                copy = old.copy()
                copy.append(number)
                addition.append(copy)
            output += addition
            
        return output
