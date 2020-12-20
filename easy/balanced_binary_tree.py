# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(h) space where h is the height of the tree
    def isBalanced(self, root: TreeNode) -> bool:
    # A Tree is balanced if the left and right subtrees differ in height by no more than one
    # We need to check the following:
    # 1) Left substree is balanced
    # 2) Right subtree is balanced
    # 3) Height of left subtree and right subtree differ by no more than one
    # Therefore we need to bubble up if a tree is balanced as well as its height
        return self.isBalancedRecursionHeight(root)[0]
        
    def isBalancedRecursionHeight(self, root):
        if root == None:
            return [True, -1]
        
        left_tree_data = self.isBalancedRecursionHeight(root.left)
        right_tree_data = self.isBalancedRecursionHeight(root.right)
        
        if not left_tree_data[0] or not right_tree_data[0]:
            return [False]
        
        if abs(left_tree_data[1] - right_tree_data[1]) > 1:
            return [False]
        
        return [True, 1 + max(left_tree_data[1], right_tree_data[1])]
