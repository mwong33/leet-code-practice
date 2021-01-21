class Solution:
    # Top Down Memo - O(prices^2) time O(prices^2) space
    def maxProfit(self, prices: List[int]) -> int:
        return self.maxProfitMemo(prices, 0, float('inf'), {})
        
    def maxProfitMemo(self, prices, index, stock, cache):
        if (index, stock) in cache:
            return cache[(index, stock)]
        
        # Base/Out of bounds Case
        if index >= len(prices):
            return 0
        
        # Choose to buy stock
        buy = self.maxProfitMemo(prices, index+1, prices[index], cache)
        
        # Choose to sell stock
        sell = (prices[index] - stock) + self.maxProfitMemo(prices, index+2, float('inf'), cache)
        
        # Do nothing
        do_nothing = self.maxProfitMemo(prices, index+1, stock, cache)
        
        cache[(index, stock)] = max(buy, sell, do_nothing)
        return cache[(index, stock)]
