class Solution:
    # O(n) space O(n) time
    def singleNumber(self, nums: List[int]) -> int:
        integer_dict = {}
        for number in nums:
            if number not in integer_dict:
                integer_dict[number] = 1
            else:
                integer_dict[number] += 1
                
        for number in nums:
            if integer_dict[number] == 1:
                return number
