class Solution:
    # Trivial O(n) time O(1) space
    def searchRangeLinear(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
                
        for i in range(len(nums)):
            if nums[i] == target and output[0] != -1:
                output[1] = i
            elif nums[i] == target:
                output[0] = i
                output[1] = i
            
        return output
