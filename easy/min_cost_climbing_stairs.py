class Solution:
    # O(n) time O(1) space
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        previous = cost[1]
        previous_2 = cost[0]
         
        for index in range(2, len(cost)):
            temp = previous
            previous = min(previous_2, previous) + cost[index]
            previous_2 = temp
            
        return min(previous, previous_2)
    
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
