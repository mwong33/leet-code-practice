# O(n) time O(1) space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        rolling_max = nums[0]
        past_max = nums[0]
        past_min = nums[0]
        
        for index in range(1,len(nums)):
            option1 = nums[index]
            option2 = nums[index] * past_max
            option3 = nums[index] * past_min
            
            past_max = max(option1, option2, option3)
            past_min = min(option1, option2, option3)
            
            if past_max > rolling_max:
                rolling_max = past_max
                
        return rolling_max
        
"""

Bottom Up:

2, -5, -2, -4, 3
2, -5, 20,  8, 24 
2,-10, -2,-80,-240

"""
