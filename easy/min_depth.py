from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        depth = 1
        
        if root.left == None and root.right == None:
            return depth
        
        left_depth = None
        right_depth = None
        
        if root.left != None:
            left_depth = self.minDepth(root.left)
        
        if root.right != None:
            right_depth = self.minDepth(root.right)
            
        if left_depth != None and right_depth != None:
            if left_depth < right_depth:
                depth += left_depth
            else:
                depth += right_depth
        elif left_depth == None:
            depth += right_depth
        else:
            depth += left_depth
            
        return depth
