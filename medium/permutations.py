class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        if len(nums) == 2:
            return [nums, nums[::-1]]
        
        permutation_list = []
        
        for i in range(len(nums)):
            grouped_list = self.permute(nums[0:i] + nums[i+1:len(nums)])
            
            for j in range(len(grouped_list)):
                grouped_list[j] = [nums[i]] + grouped_list[j]
            
            permutation_list += grouped_list
        
        return permutation_list
