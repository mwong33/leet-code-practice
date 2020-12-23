class Solution:
    # O(n) time O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        # Greedy Algorithm, buy low, sell high
        if len(prices) <= 1:
            return 0
        
        current_min = prices[0]
        max_profit = 0
        
        for i in range(1,len(prices)):
            if prices[i] > current_min:
                max_profit += (prices[i] - current_min)
                current_min = prices[i]
            elif prices[i] < current_min:
                current_min = prices[i]
                
        return max_profit
