class Solution:
    # Top Down Memo - O(nums*S) time O(nums*S) space
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        return self.findTargetSumWaysMemo(nums, S, 0, 0, {})
    
    def findTargetSumWaysMemo(self, nums, target, index, total, cache):
        if (index, total) in cache:
            return cache[(index, total)]
        
        # Base Case
        if index == len(nums):
            if total == target:
                return 1
            else:
                return 0
            
        # Consider the plus and minus option
        plus_option = self.findTargetSumWaysMemo(nums, target, index+1, total+nums[index], cache)
        minus_option = self.findTargetSumWaysMemo(nums, target, index+1, total-nums[index], cache)
        
        cache[(index, total)] = plus_option + minus_option
        
        return plus_option + minus_option
