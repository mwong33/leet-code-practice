# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) time O(n^2) space
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(0, 0, len(inorder) - 1, preorder, inorder)
    
    def buildTreeHelper(self, preStart, inStart, inEnd, preorder, inorder):
        if len(preorder) == 0 or preStart >= len(preorder) or inStart > inEnd:
            return None
        
        root = TreeNode(preorder[preStart])
        
        inIndex = 0
        
        for i in range(inEnd+1):
            if inorder[i] == root.val:
                inIndex = i
                break
                
        root.left = self.buildTreeHelper(preStart + 1, inStart, inIndex - 1, preorder, inorder)
        root.right = self.buildTreeHelper(preStart + inIndex - inStart + 1, inIndex + 1, inEnd, preorder, inorder)
        
        return root
