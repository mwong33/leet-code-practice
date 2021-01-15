class Solution:
    # Top Down Memo - O(d*f) time O(d*f) space 
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.numRollsToTargetMemo(f, target, 0, d, {}) % (10**9 + 7)
    
    def numRollsToTargetMemo(self, f, target, current_sum, dice_remaining, cache):
        if (current_sum, dice_remaining) in cache:
            return cache[(current_sum, dice_remaining)]
        
        # Base Cases
        if current_sum == target and dice_remaining == 0:
            return 1
        
        if dice_remaining == 0:
            return 0
        
        # Choose a dice value        
        options = 0
        for i in range(1, f+1):
            options += self.numRollsToTargetMemo(f, target, current_sum+i, dice_remaining-1, cache)
        
        cache[(current_sum, dice_remaining)] = options
        return options
