# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(h) space where h is the height of the tree
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:        
        return self.dfs(root, targetSum, 0)
    
    def dfs(self, root, target, current):
        if root == None:
            return False
        
        current += root.val
        
        # Base Cases
        if root.left == None and root.right == None:
            if current == target:
                return True
            else:
                return False

        return self.dfs(root.left, target, current) or self.dfs(root.right, target, current)
