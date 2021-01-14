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
    
    # O(n) time O(n) space
    def minCostClimbingStairsTable(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
         
        for index in range(2, len(cost)):
            dp[index] = min(dp[index-1], dp[index-2]) + cost[index]
            
        return min(dp[-1], dp[-2])
