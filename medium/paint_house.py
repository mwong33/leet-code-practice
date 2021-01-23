class Solution:
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
