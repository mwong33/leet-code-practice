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
        
        majority_num = None
        
        for i in count_table.keys():
            if majority_num == None or count_table[i] > count_table[majority_num]:
                majority_num = i
            
        return majority_num
