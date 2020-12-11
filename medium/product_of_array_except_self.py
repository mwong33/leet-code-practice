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
    
    # O(1) space and O(n) time given result array does not count for memory
    def productExceptSelfConstantSPace(self, nums: List[int]) -> List[int]:
        result = [1]
        
        for i in range(len(nums) - 1):
            result.append(result[len(result) - 1] * nums[i])
                    
        right_multiple = 1
            
        for i in reversed(range(len(nums))):
            result[i] = result[i] * right_multiple
            right_multiple = right_multiple * nums[i]
            
        return result
