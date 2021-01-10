# O(n^2) time O(n) space
class Solution:
    def robSquaredTimeLinearSpace(self, nums: List[int]) -> int:
        # Iterate through each house
        # Determine the max amount of money we can make if we stopped at that house
        # To do this, look at all houses before the house we are stopping at excluding the one right before it
        # Choose the house with the largest amount of money and add it to the value of the house we are stopping at
        # Continue this loop until we finish looking at all houses
        # Return the maximum of our array we use to store the steal value of each house
        if len(nums) == 0:
            return 0
        
        rob_house = [0] * len(nums)
        
        for i in range(len(nums)):
            value = nums[i]
            for j in range(i-2, -1, -1):
                if rob_house[j] + nums[i] > value:
                    value = rob_house[j] + nums[i]
            rob_house[i] = value

        return max(rob_house)
        
"""
Bottom Up

1, 10, 20,  4, 2,  10
1, 10, 21, 14, 23, 31

4, 1, 1, 4
4, 1, 5, 8

"""

# O(n) time O(n) space
class Solution:
    def robLinearTimeLinearSpace(self, nums: List[int]) -> int:
        # Iterate through each house
        # Determine the max amount of money we can make if we stopped at that house
        # To do this, look at the previous two houses. Take the max of either just the previous house (not robbing the house we are at)
        # or adding our house value to the value of two houses before it
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        rob_house_array = [0] * len(nums)
        rob_house_array[0] = nums[0]
        rob_house_array[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            skip_house = rob_house_array[i-1]
            rob_house = nums[i] + rob_house_array[i-2]
            
            max_value = max(skip_house, rob_house)
            
            rob_house_array[i] = max_value
            
        return max(rob_house_array)

# O(n) time O(1) space
class Solution:
    def robLinearTimeConstantSpace(self, nums: List[int]) -> int:
        # Iterate through each house
        # Determine the max amount of money we can make if we stopped at that house
        # To do this, look at the previous two houses. Take the max of either just the previous house (not robbing the house we are at)
        # or adding our house value to the value of two houses before it
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        past_2 = nums[0]
        past_1 = max(nums[0], nums[1])
        rolling_max = past_1
        
        for i in range(2, len(nums)):
            skip_house = past_1
            rob_house = past_2 + nums[i]
            
            max_value = max(skip_house, rob_house)
            
            past_2 = past_1
            past_1 = max_value
            
            if max_value > rolling_max:
                rolling_max = max_value
            
        return rolling_max
