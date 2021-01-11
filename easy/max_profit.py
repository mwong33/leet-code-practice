class Solution:
    # O(n) time O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        # Keep track of the minimum digit with a rolling number
        # Keep track of the maximum profit with a rolling number
        # starting with the second digit loop through each digit
        # 1) given the current minimum digit see if our current digit exceeds it
        # 2) if it does check the profit and compare it with our current profit (initially set to 0)
        # 3) if it is greater than the current profit, replace the current profit with our new profit value
        # 4) see if our current digit is less than the current minimum. If it is, replace the minimum with our current minimum
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        min_digit = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] > min_digit:
                current_profit = prices[i] - min_digit
                if current_profit > max_profit:
                    max_profit = current_profit
            
            if prices[i] < min_digit:
                min_digit = prices[i]
                       
        return max_profit
