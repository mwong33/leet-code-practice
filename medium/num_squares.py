class Solution:
    # Top Down Memo - O(n) time O(n) space
    def numSquares(self, n: int) -> int:
        return self.numSquaresMemo(n, {})
    
    def numSquaresMemo(self, remaining, cache):
        if remaining in cache:
            return cache[remaining]
        
        # Base Cases
        if remaining == 0:
            return 0
        
        if remaining < 0:
            return False
        
        min_option = False
        for i in range(1, remaining+1):
            if i*i <= remaining:
                potential_option = self.numSquaresMemo(remaining-(i*i), cache)
                if potential_option == 0 or potential_option != False:
                    if min_option == False or min_option > 1+ potential_option:
                        min_option = 1 + potential_option
            else:
                break
        
        cache[remaining] = min_option
        return min_option
    
    # Bottom Up Table - O(n * m) time O(n) space where m is the largest square number less than or equal to n
    def numSquaresBottomUp(self, n: int) -> int:
        # Create a remainder_array of length n+1 and fill it with None
        # Loop from 0 to n
        # For each digit determine the minimum number of square numbers to form it
        # Do this by checking each square number less than or equal to the digit we are checking for and get the difference
        # Use out table array to check how many more min square numbers we'll need to finish off the difference
        # Eventually assign the table array value for the digit we are checking with the minimum sum we can get given we try all 
        # possible perfect squares that are less than or equal to the digit
        table = [None] * (n+1)
        table[0] = 0
        
        for number in range(1,n+1):
            sq_num = 1
            min_value = table[number]
            while (sq_num*sq_num) <= number:
                difference = number - (sq_num*sq_num)
                potential_value = 1 + table[difference]
                
                if table[number] == None or table[number] > potential_value:
                    table[number] = potential_value
                
                sq_num += 1
                
        return table[-1]
        
"""

Bottom Up:

n = 12 options = [1, 4, 9, 16, 25]

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 
0, 1, 2, 3, 1, 2, 3, 4, 2, 1,  2,  3,  3

"""
