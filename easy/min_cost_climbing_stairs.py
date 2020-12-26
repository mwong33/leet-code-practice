class Solution:
    # O(n) time, O(1) space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first_option = 0
        second_option = 0
        
        for x in reversed(cost):
            temp = first_option
            first_option = x + min(first_option, second_option)
            second_option = temp
            
        return min(first_option, second_option)
