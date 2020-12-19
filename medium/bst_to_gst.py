# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(n) space
    def bstToGst(self, root: TreeNode) -> TreeNode:
        sorted_array = self.convertBstToSortedArray(root)
        sorted_array_sum = 0
        
        while len(sorted_array) != 0:
            node = sorted_array.pop()
            sorted_array_sum += node.val
            node.val = sorted_array_sum
            
        return root
    
    def convertBstToSortedArray(self, root):
        if root == None:
            return []
        
        sorted_array = []
        
        if root.left != None:
            sorted_array += self.convertBstToSortedArray(root.left)
            
        sorted_array.append(root)
        
        if root.right != None:
            sorted_array += self.convertBstToSortedArray(root.right)
            
        return sorted_array
