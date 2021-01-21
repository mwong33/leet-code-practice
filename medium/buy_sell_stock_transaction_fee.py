class Solution:
    # Bottom Up - O(n) time O(1) space by brianchiang_tw
    def maxProfitBottomUp(self, prices: List[int], fee: int) -> int:
        not_hold_value = 0
        hold_value = -float('inf')
        
        for stock_price in prices:
            prev_not_hold_value = not_hold_value
            prev_hold_value = hold_value
            
            # Sell stock at current price or stick with current not_hold_value
            not_hold_value = max(prev_not_hold_value, stock_price + prev_hold_value)
            
            # Buy stock at current price or keep stock with current hold value
            hold_value = max(prev_hold_value, prev_not_hold_value - stock_price - fee)
            
        return not_hold_value
            
"""
          sell (+ hold_value)
          -->
hold               not_hold
          <--      
          buy ( - stock_price + fee)

Ex:

fee = 2
                      1   3   2   8   4   9
not_hold_value  0     0   0   0   5   5   8
hold_value     -inf  -3  -3  -3  -3  -1  -1    
"""
    
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
