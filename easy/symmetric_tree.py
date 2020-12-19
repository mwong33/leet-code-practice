# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        if root.left == None and root.right == None:
            return True
        
        return self.compareTrees(root.left, root.right)
        
    def compareTrees(self, left, right):
        if left == None and right == None:
            return True
        
        if left == None or right == None:
            return False
        
        if left.val != right.val:
            return False
            
        side_one = self.compareTrees(left.left, right.right)
        side_two = self.compareTrees(left.right, right.left)
        
        return side_one and side_two
