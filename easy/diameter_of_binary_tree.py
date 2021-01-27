# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(n) space
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return self.dfs(root)[0]
        
    def dfs(self, root):
        # Base Case
        if root == None:
            return (0, 0)

        left_result = self.dfs(root.left)
        right_result = self.dfs(root.right)
        
        diameter = max(left_result[0], right_result[0], left_result[1] + right_result[1])
        return (diameter, max(left_result[1], right_result[1]) + 1)
    
"""
diameter = max(L Diameter, R Diameter, LMax + RMax)
return (diameter, max(LMax, RMax)+1)
"""
