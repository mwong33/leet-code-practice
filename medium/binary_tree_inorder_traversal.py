# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(n) space if you count the array we are returning
    def inorderTraversalRecursion(self, root: TreeNode) -> List[int]:
        # inorder traversal - left, node, right
        # We can traverse the array in inorder traversal with recursion
        if root == None:
            return []
        
        left_sub_tree = self.inorderTraversalRecursion(root.left)
        right_sub_tree = self.inorderTraversalRecursion(root.right)
        
        return left_sub_tree + [root.val] + right_sub_tree
