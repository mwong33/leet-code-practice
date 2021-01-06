# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        return self.equals(s,t) or (s != None and self.isSubtree(s.left, t)) or (s != None and self.isSubtree(s.right, t))
    
    # Helper function to determine if two trees are identical
    def equals(self, s, t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.val != t.val:
            return False
        
        return s.val == t.val and self.equals(s.left, t.left) and self.equals(s.right, t.right)
