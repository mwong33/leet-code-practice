class Solution:
    # Top Down Memo - O(n*sum) time O(n*sum) space
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total%2 != 0:
            return False
        
        half = total//2       
        return self.canPartitionMemo(nums, half, 0, 0, {})
    
    def canPartitionMemo(self, nums, half, current_sum, index, cache):
        if (current_sum, index) in cache:
            return cache[(current_sum, index)]
        
        # Base Cases
        if current_sum == half:
            return True
        
        if index >= len(nums):
            return False
        
        if nums[index] == half:
            return True
        
        if nums[index] > half:
            return False
        
        # Choose or not choose number
        choose = self.canPartitionMemo(nums, half, current_sum + nums[index], index+1, cache)
        ignore = self.canPartitionMemo(nums, half, current_sum, index+1, cache)
        
        cache[(current_sum, index)] = choose or ignore
        return choose or ignore
