# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time O(n) space
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # Step One: Convert Tree to inorder array
        inorder_array = self.convertToArray(root)
        
        # Step Two: Check to see if the inorder_array is sorted
        for index in range(1, len(inorder_array)):
            if inorder_array[index - 1] >= inorder_array[index]:
                return False
            
        return True
        
    def convertToArray(self, root):
        if root == None:
            return []
        
        left_array = self.convertToArray(root.left)
        right_array = self.convertToArray(root.right)
        
        return left_array + [root.val] + right_array
