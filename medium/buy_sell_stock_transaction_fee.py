class Solution:
    # Top Down Memo - O(n) time O(n^2) space (Time Out)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
                
        return self.maxProfitMemo(prices, fee, 0, 0, {})
    
    def maxProfitMemo(self, prices, fee, index, previous_stock, cache):
        if (index, previous_stock) in cache:
            return cache[(index, previous_stock)]
        
        # Base Case
        if index == len(prices) - 1:
            sell = -1
            if previous_stock != 0:
                sell = prices[index] - previous_stock - fee            
            return max(sell, -1 * previous_stock)
        
        # Just Buy Stock
        just_buy_stock = -1
        if previous_stock == 0:
            just_buy_stock = self.maxProfitMemo(prices, fee, index+1, prices[index], cache)
        
        # Just Sell Stock
        just_sell = -1
        if previous_stock != 0:
            just_sell = (prices[index] - previous_stock - fee) + self.maxProfitMemo(prices, fee, index+1, 0, cache)
                
        # Do nothing
        do_nothing = self.maxProfitMemo(prices, fee, index+1, previous_stock, cache)
        
        cache[(index, previous_stock)] = max(just_buy_stock, just_sell, do_nothing)
        return cache[(index, previous_stock)]
