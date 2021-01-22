class Solution:
    # Top Down Memo -
    def stoneGame(self, piles: List[int]) -> bool:
        result = self.stoneGameMemo(piles, 0, len(piles)-1, 1, {})
        if result[0] > result[1]:
            return True
        
        return False
        
    def stoneGameMemo(self, piles, start, end, turn, cache):
        if (start, end, turn) in cache:
            return cache[(start, end, turn)]
        
        # Base Case (Last Turn)
        if turn == len(piles):
            return [0, piles[start]]
        
        left_outcome = self.stoneGameMemo(piles, start+1, end, turn+1, cache)
        right_outcome = self.stoneGameMemo(piles, start, end-1, turn+1, cache)
        
        # Alex's turn
        if turn%2 != 0:
            choose_start = [left_outcome[0]+piles[start], left_outcome[1]]
            choose_end = [right_outcome[0]+piles[end], right_outcome[1]]
            
            if choose_start[0] > choose_end[0]:
                cache[(start, end, turn)] = choose_start
                return choose_start
            
            cache[(start, end, turn)] = choose_end
            return choose_end
            
        # Lee's Turn
        else:
            choose_start = [left_outcome[0], left_outcome[1] + piles[start]]
            choose_end = [right_outcome[0], right_outcome[1] + piles[end]]
            
            if choose_start[1] > choose_end[1]:
                cache[(start, end, turn)] = choose_start
                return choose_start
            
            cache[(start, end, turn)] = choose_end
            return choose_end
        
        
"""
Top Down Recursive Brute Force

piles = [5,3,4,5]


1.                    5 or 5
                     /         \ 
2.               3 or 5       5 or 4 
                /      \       /    \
3.            4 or 5  3 or 4  3 or 4  5 or 3  

4. Pick the last choice

1. Alex's Turn   
2. Lee's Turn
3. Alex's Turn'
4. Lee's turn

On odd turns, add stones, on even turns add stones. For each turn we try to maximize our return value which will be 
The max scores for both alex and lee
"""
