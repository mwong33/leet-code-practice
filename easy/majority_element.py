class Solution:
    # O(n) time O(n) space
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        count_table = {}
        
        for number in nums:
            if number not in count_table:
                count_table[number] = 1
            else:
                count_table[number] += 1
                
        for i in count_table.keys():
            if count_table[i] > len(nums)/2:
                return i
    
    # O(n) time O(1) space Boyer-Moore Voting Algorithm
    def majorityElementBM(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        
        for number in nums:
            if number == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = number
                    count = 1
            
        return candidate
