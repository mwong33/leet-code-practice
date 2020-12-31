class Solution:
    # O(n) time O(1) space
    def removeDuplicates(self, nums: List[int]) -> int:
        # Set the variable current_num to the first element of the array
        # 1) Start with the fast index at the second element of the array in a while loop
        # 2) Start the slow index at the second element of the array in the same while loop
        # 3) check if that element is the same as current_num or less than the current_num, if it is iterate
        #    if not, swap the fast index's element with the slow index's element. Set current element to 
        #    slow index's element. Iterate slow index and fast index
        if len(nums) == 0:
            return 0
        
        slow_index = 1
        fast_index = 1
        current_num = nums[0]
        
        while fast_index < len(nums):
            if nums[fast_index] > current_num:
                temp = nums[slow_index]
                nums[slow_index] = nums[fast_index]
                nums[fast_index] = temp
                
                current_num = nums[slow_index]
                slow_index += 1
                
            fast_index += 1
            
        return len(nums[:slow_index])
