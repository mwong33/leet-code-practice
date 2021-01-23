class Solution:
    # Bottom Up Table - O(nums) time O(1) space
    def robOptimum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        prev_chose_first = nums[0]
        prev_not_first = 0
        
        chose_first = max(nums[0], nums[1])
        not_first = nums[1]
        
        for i in range(2, len(nums)):
            temp_chose_first = chose_first
            temp_not_first = not_first
            
            # Last house edge case
            if i == len(nums)-1:
                chose_first = temp_chose_first
                not_first = max(nums[i] + prev_not_first, not_first)
            else:
                chose_first = max(nums[i] + prev_chose_first, temp_chose_first)
                not_first = max(nums[i] + prev_not_first, not_first)
                
                prev_chose_first = temp_chose_first
                prev_not_first = temp_not_first
        
        return max(chose_first, not_first)
     
    # Bottom Up Table - O(nums) time O(nums) space
    def robTable(self, nums: List[int]) -> int:
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
