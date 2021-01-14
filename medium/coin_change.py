class Solution:
    # Top Down Memo - O(coins * amount) time O(amount) space
    def coinChangeTopDown(self, coins: List[int], amount: int) -> int:
        cache = {}
        return self.coinChangeMemo(coins, amount, 0, cache)
    
    def coinChangeMemo(self, coins, amount, current_amount, cache):
        if current_amount in cache:
            return cache[current_amount]
        
        if current_amount == amount:
            return 0
        
        min_choice = -1
            
        for coin in coins:
            if coin <= amount - current_amount:
                potential_choice = self.coinChangeMemo(coins, amount, current_amount + coin, cache)
                
                if min_choice != -1 and potential_choice != -1:
                    if min_choice > potential_choice:
                        min_choice = 1 + potential_choice
                elif min_choice == -1 and potential_choice != -1:
                    min_choice = 1 + potential_choice
        
        cache[current_amount] = min_choice
        return min_choice
        
    # Bottom Up Table - O(coins * amount) time O(amount) space 
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [-1] * (amount+1)
        table[0] = 0
        
        for value in range(1, amount+1):
            # Loop through each value up to amount
            # Deduct each coin that is less than or equal to value
            # Add 1 +  table[remainder] where remainder = value - coin
            # Set the minimum of 1+ table[remainder] to table[value]
            curr_count = -1
            for coin in coins:
                if coin <= value:
                    remainder = value - coin
                    if table[remainder] != -1:
                        if curr_count == -1:
                            curr_count = 1 + table[remainder]
                        elif curr_count > 1 + table[remainder]:
                            curr_count = 1 + table[remainder]
            
            table[value] = curr_count
            
        return table[amount]

"""
Bottom Up:

coins = [1,2,5], amount = 11

0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11

0,  1,  1,  2,  2,  1,  2,  2,  3,  3,  2,  3


coins = [2, 5], amound = 11

0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11

0, -1,  1, -1,  2,  1,  3,  2,  4,  3,  2,  4

"""
