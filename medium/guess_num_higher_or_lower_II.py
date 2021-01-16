import math

class Solution:
    # Top Down Memo
    def getMoneyAmount(self, n: int) -> int:
        return self.getMoneyAmountMemo(1, n, {})
    
    def getMoneyAmountMemo(self, lower_bound, upper_bound, cache):
        if (lower_bound, upper_bound) in cache:
            return cache[(lower_bound, upper_bound)]
        
        # Base Case
        if lower_bound >= upper_bound:
            return 0
                
        if upper_bound - lower_bound == 1:
            return lower_bound

        winning_strategy = float('inf')
        
        for guess in range(lower_bound, upper_bound+1):
            # Guess is too high
            too_low = guess + self.getMoneyAmountMemo(lower_bound, guess-1, cache)
            too_high = guess + self.getMoneyAmountMemo(guess+1, upper_bound, cache)
            
            winning_strategy = min(winning_strategy, max(too_low, too_high))
        
        cache[(lower_bound, upper_bound)] = winning_strategy
        return winning_strategy
