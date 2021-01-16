class Solution:
    # Top Down Memo - O(n^2) time O(n) space
    def numTrees(self, n: int) -> int:
        return self.numTreesMemo(n, {})
    
    def numTreesMemo(self, nodes_remaining, cache):
        if nodes_remaining in cache:
            return cache[nodes_remaining]
        
        # Base Case
        if nodes_remaining <= 1:
            return 1
        
        unique_trees = 0
        
        for i in range(0, nodes_remaining):
            left_subtree = self.numTreesMemo(i, cache)
            right_subtree = self.numTreesMemo(nodes_remaining-1-i, cache)
            
            unique_trees += left_subtree * right_subtree
            
        cache[nodes_remaining] = unique_trees
        return unique_trees
