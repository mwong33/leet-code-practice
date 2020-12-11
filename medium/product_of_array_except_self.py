class Solution:
    # O(n) space and O(n) time
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [1]
        
        for i in range(len(nums) - 1):
            left_array.append(left_array[len(left_array) - 1] * nums[i])
        
        right_array = [1]
        
        for i in range(len(nums) - 1, 0, -1):
            right_array.append(right_array[len(right_array) - 1] * nums[i])
            
        result = []    
            
        for i in range(len(nums)):
            result.append(left_array[i] * right_array[len(right_array) - 1 - i])
            
        return result
