class Solution:
    # Bottom Up Table - O(prices) time O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        no_stock = 0
        have_stock = -1 * prices[0]
        sold_stock = 0
        
        for index in range(1, len(prices)):
            prev_no_stock = no_stock
            prev_have_stock = have_stock
            prev_sold_stock = sold_stock
            
            no_stock = max(prev_no_stock, prev_sold_stock)
            have_stock = max(prev_have_stock, prev_no_stock - prices[index])
            sold_stock = prev_have_stock + prices[index]
        
        return max(no_stock, sold_stock)

"""
States:

1) No Stock
2) Have Stock
3) Sold Stock

No Stock -> No Stock
Sold Stock -> No Stock

Have Stock -> Have Stock
(No Stock - prices[index]) -> Have Stock

(Have Stock + prices[index]) -> Sold Stock

             1    2    3    0    2
No Stock     0    0    1    2    2
Have Stock  -1   -1   -1    1    1
Sold Stock   0    1    2   -1    3
"""
    
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
