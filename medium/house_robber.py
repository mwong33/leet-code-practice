# O(n^2) time O(n) space
class Solution:
    def rob(self, nums: List[int]) -> int:
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
