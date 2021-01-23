class Solution:
    # Bottom Up Table - O(nums) time O(nums) space
    def rob(self, nums: List[int]) -> int:
        dp = [[0] * len(nums) for _ in range(2)]
        dp[0][0] = nums[0]
        
        for i in range(1, len(nums)):
            # Last House Case
            if i == len(nums) - 1:
                dp[0][i] = dp[0][i-1]
                dp[1][i] = max(nums[i] + dp[1][i-2], dp[1][i-1])
            elif i == 1:
                dp[0][i] = max(nums[i], dp[0][i-1])
                dp[1][i] = nums[i]
            else:
                dp[0][i] = max(nums[i] + dp[0][i-2], dp[0][i-1])
                dp[1][i] = max(nums[i] + dp[1][i-2], dp[1][i-1])
                
        return max(dp[0][-1], dp[1][-1])
 
"""
                       1  2  3  1
Chose Start            1  2  4  4
Did not choose start   0  2  3  3

                       2  3  2
Chose Start            2  3  3
Did not choose start   0  3  2

"""
