class Solution:
    # Prefix Sum Hash Map - O(n) time O(n) space
    def subarraySum(self, nums: List[int], k: int) -> int:
        cumulative_sums = {0: 1}
        
        count = 0
        cumulative_sum = 0
        for index in range(len(nums)):
            cumulative_sum = cumulative_sum + nums[index]
            
            if cumulative_sum - k in cumulative_sums:
                count += cumulative_sums[cumulative_sum - k]
            
            if cumulative_sum not in cumulative_sums:
                cumulative_sums[cumulative_sum] = 1
            else:
                cumulative_sums[cumulative_sum] += 1
        
        return count
