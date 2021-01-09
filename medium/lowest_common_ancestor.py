# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# O(n) time O(1) space
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # If you are None, return None
        # If you are one of the values, p or q, return yourself
        # If both subtrees are None, return None
        # If only one subtree is not None, return that node
        # If both subtrees are not None, return yourself
        
        if root == None:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        left_sub_tree = self.lowestCommonAncestor(root.left, p, q)
        right_sub_tree = self.lowestCommonAncestor(root.right, p, q)
        
        if left_sub_tree == None and right_sub_tree == None:
            return None
        
        if left_sub_tree != None and right_sub_tree != None:
            return root
        
        if left_sub_tree != None:
            return left_sub_tree
        else:
            return right_sub_tree
