# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if root.left == None and root.right== None:
            return root
        
        sorted_array = self.convertBSTtoSortedArray(root)
        
        return self.convertArrayToBST(sorted_array)
        
    def convertBSTtoSortedArray(self, root):        
        if root == None:
            return []
        
        sorted_array = []
        
        if root.left != None:
            sorted_array += self.convertBSTtoSortedArray(root.left)
            
        sorted_array.append(root.val)
        
        if root.right != None:
            sorted_array += self.convertBSTtoSortedArray(root.right)
            
        return sorted_array
    
    def convertArrayToBST(self, array):
        if len(array) == 0:
            return None
        
        halfway = len(array)//2
        
        parent = TreeNode(array[halfway])
        
        parent.left = self.convertArrayToBST(array[:halfway])
        parent.right = self.convertArrayToBST(array[halfway+1:])
        
        return parent
