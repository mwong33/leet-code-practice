class Solution:
    # O(n) time O(n) space Top Down Memo
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        return min(self.minCostClimbingStairsMemo(cost, len(cost)-1, cache), self.minCostClimbingStairsMemo(cost, len(cost)-2, cache))
        
    def minCostClimbingStairsMemo(self, cost, index, cache):
        if index in cache:
            return cache[index]
        
        if index == 1:
            return cost[1]
        
        if index == 0:
            return cost[0]
        
        result = cost[index] + min(self.minCostClimbingStairsMemo(cost, index-1, cache), self.minCostClimbingStairsMemo(cost, index-2, cache))
        cache[index] = result
        
        return result
    
    # O(n) time O(1) space Bottom Up Variables
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
    
    # O(n) time O(n) space Bottom Up Table
    def minCostClimbingStairsTable(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)
        
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
         
        for index in range(2, len(cost)):
            dp[index] = min(dp[index-1], dp[index-2]) + cost[index]
            
        return min(dp[-1], dp[-2])
