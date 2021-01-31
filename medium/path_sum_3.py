# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(n) space
    def pathSum(self, root: TreeNode, sum: int) -> int:
        cache = {0: 1}
        return self.dfs(root, sum, 0, cache)
    
    def dfs(self, root, target, cumulative_sum, cache):
        if root == None:
            return 0
        
        cumulative_sum += root.val
        difference = cumulative_sum - target
        result = 0
        
        if difference in cache:
            result += cache[difference]
            
        if cumulative_sum not in cache:
            cache[cumulative_sum] = 1
        else:
            cache[cumulative_sum] += 1

        left_result = result + self.dfs(root.left, target, cumulative_sum, cache) 
        right_result = self.dfs(root.right, target, cumulative_sum, cache)
        
        cache[cumulative_sum] -= 1
        
        return left_result + right_result
