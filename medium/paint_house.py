class Solution:
    # Bottom Up Table - O(costs) time O(costs) space
    def minCostTable(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        
        dp = [[0] * len(costs) for _ in range(3)]
        dp[0][0] = costs[0][0]
        dp[1][0] = costs[0][1]
        dp[2][0] = costs[0][2]
        
        for i in range(1, len(costs)):
            # Best Red Choice
            dp[0][i] = costs[i][0] + min(dp[1][i-1], dp[2][i-1])
            
            # Best Blue Choice
            dp[1][i] = costs[i][1] + min(dp[0][i-1], dp[2][i-1])
            
            # Best Green Choice
            dp[2][i] = costs[i][2] + min(dp[0][i-1], dp[1][i-1])
            
        return min(dp[0][-1], dp[1][-1], dp[2][-1])
"""
0 - red 
1 - blue 
2 - green

         1    2    3
red     17   18   21  
blue     2   33   10 
green   17    7   37 
"""
    
    # Recursive Memo - O(costs) time O(costs) space
    def minCost(self, costs: List[List[int]]) -> int:
        if len(costs) == 0:
            return 0
        
        return self.minCostMemo(costs, 0, -1, {})
    
    def minCostMemo(self, costs, index, previous_color, cache):
        if (index, previous_color) in cache:
            return cache[(index, previous_color)]
        
        # Base Case
        if index == len(costs) - 1:
            options = []
            for i in range(3):
                if i != previous_color:
                    options.append(costs[index][i])
                    
            return min(options)
        
        # Normal Case
        if previous_color == -1:
            choose_red = costs[index][0] + self.minCostMemo(costs, index+1, 0, cache)
            choose_blue = costs[index][1] + self.minCostMemo(costs, index+1, 1, cache)
            choose_green = costs[index][2] + self.minCostMemo(costs, index+1, 2, cache)
            
            cache[(index, previous_color)] = min(choose_red, choose_blue, choose_green)
            return cache[(index, previous_color)]
        elif previous_color == 0:
            choose_blue = costs[index][1] + self.minCostMemo(costs, index+1, 1, cache)
            choose_green = costs[index][2] + self.minCostMemo(costs, index+1, 2, cache)
            
            cache[(index, previous_color)] = min(choose_blue, choose_green)
            return cache[(index, previous_color)]
        elif previous_color == 1:
            choose_red = costs[index][0] + self.minCostMemo(costs, index+1, 0, cache)
            choose_green = costs[index][2] + self.minCostMemo(costs, index+1, 2, cache)
            
            cache[(index, previous_color)] = min(choose_red, choose_green)
            return cache[(index, previous_color)]
        else:
            choose_red = costs[index][0] + self.minCostMemo(costs, index+1, 0, cache)
            choose_blue = costs[index][1] + self.minCostMemo(costs, index+1, 1, cache)
            
            cache[(index, previous_color)] = min(choose_red, choose_blue)
            return cache[(index, previous_color)]
        
"""
0 - red 
1 - blue 
2 - green
"""
