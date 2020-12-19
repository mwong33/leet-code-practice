# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(1) space O(n) time
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None or q == None:
            if p == q:
                return True
            else:
                return False
        
        # Check current val
        if p.val != q.val:
            return False
        
        # Check Left Subtree
        is_left_same = self.isSameTree(p.left, q.left)
        
        # Check Right Subtree
        is_right_same = self.isSameTree(p.right, q.right)
        
        return is_left_same and is_right_same
