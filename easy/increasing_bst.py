# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time
    def increasingBST(self, root: TreeNode) -> TreeNode:
        sorted_array = self.convertBSTtoSortedArray(root)
        
        increasing_bst = TreeNode(sorted_array[0])
        temp_pointer = increasing_bst
        
        for i in range(1,len(sorted_array)):
            temp_pointer.right = TreeNode(sorted_array[i])
            temp_pointer = temp_pointer.right
            
        return increasing_bst
            
    def convertBSTtoSortedArray(self, root):
        if root == None:
            return []
        
        sorted_array = self.convertBSTtoSortedArray(root.left)
        sorted_array.append(root.val)
        sorted_array += self.convertBSTtoSortedArray(root.right)
        
        return sorted_array
