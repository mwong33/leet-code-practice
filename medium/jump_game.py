class Solution: 
    # O(n) time O(1) space, credit to MidhileshMomidi
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        for i in range(len(nums)):
            if max_index >= len(nums) - 1:
                return True
            
            if max_index < i:
                return False
            else:
                max_index = max(max_index,i+nums[i])
        return True
