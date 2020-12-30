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
    
    # O(logn) time O(1) space
    # Binary Search the higher element and smaller element
    def searchRangeBinary(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        
        if len(nums) == 0: 
            return output
        
        if nums[0] == target: 
            output[0] = 0
        else:
            # Binary Search Lower Bound
            output[0] = self.binarySearchLessThan(nums, target)
            
        if nums[len(nums)-1] == target:
            output[1] = len(nums) - 1
        else:        
            # Binary Search Upper Bound
            output[1] = self.binarySearchGreaterThan(nums, target)
            
        return output
    
    def binarySearchLessThan(self, nums, target):
        index = -1
        start = 0
        end = len(nums) -1
        
        while start <= end:
            middle = (end + start)//2
            
            if nums[middle] == target:
                index = middle
            
            if nums[middle] >= target:
                end = middle - 1
            elif nums[middle] < target:
                start = middle + 1
        
        return index
    
    def binarySearchGreaterThan(self, nums, target):
        index = -1
        start = 0
        end = len(nums) -1
        
        while start <= end:
            middle = (end + start)//2
            if nums[middle] == target:
                index = middle
            
            if nums[middle] > target:
                end = middle - 1
            elif nums[middle] <= target:
                start = middle + 1
        return index
