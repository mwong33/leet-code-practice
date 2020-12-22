class Solution:
    # O(n) time O(1) space
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Iterate through each digit:
        # 1) Check digit on its own
        # 2) Compare it with the optimal continguous array before it
        # 3) Either keep the digit on its own or add the contiguous array before it
        
        current_max = None
        moving_max = None
        
        for digit in nums:
            if current_max == None:
                current_max = digit
                moving_max = digit
            else:
                moving_max = max(digit, digit + moving_max)
            
            if moving_max > current_max:
                current_max = moving_max
                
        return current_max
