# O(n^2) time O(n) space brute force
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Check every substring of nums to see if their sums are a multiple of k
        # Make sum calculation constant by remembering the sum of the previous sum
        for i in range(1, len(nums)):
            past_sum = nums[i-1]
            for j in range(i, len(nums)):
                total = past_sum + nums[j]
                if total == k or total == 0:
                    return True
                if k != 0 and total >= k and total%k == 0:
                    return True
                
                past_sum = total
                
        return False
