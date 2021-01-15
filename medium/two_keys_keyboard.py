class Solution:
    # Top Down Memo - O(n) time O(n^2) space
    def minSteps(self, n: int) -> int:
        return self.minStepsMemo(n, 1, 0, {})
    
    def minStepsMemo(self, target, a_count, a_copied, cache):
        if (a_count, a_copied) in cache:
            return cache[(a_count, a_copied)]
        
        # Base Cases
        if a_copied > target or a_count > target:
            return 2000
        
        if a_count == target:
            return 0
        
        # Copy Option
        copy_option = 2000
        if a_count != a_copied:
            copy_option = 1 + self.minStepsMemo(target, a_count, a_count, cache)
        
        # Paste Option
        paste_option = 2000
        if a_copied != 0:
            paste_option = 1 + self.minStepsMemo(target, a_count+a_copied, a_copied, cache)
        
        result = min(copy_option, paste_option)
        cache[(a_count, a_copied)] = result
        return result
