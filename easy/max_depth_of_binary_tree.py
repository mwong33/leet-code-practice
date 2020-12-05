# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time where n is the number of nodes
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 1

        left_branch_depth = self.maxDepth(root.left)
        right_branch_depth = self.maxDepth(root.right)
        
        if left_branch_depth > right_branch_depth:
            return 1 + left_branch_depth
        else:
            return 1 + right_branch_depth
