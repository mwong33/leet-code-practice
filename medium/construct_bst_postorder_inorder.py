# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n^2) time O(n) space (where n is the number of nodes to construct the tree we are returning)
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        return self.buildTreeHelper(len(postorder)-1, 0, len(inorder)-1, inorder, postorder)
    
    def buildTreeHelper(self, postIndex, inStart, inEnd, inorder, postorder):
        if len(postorder) == 0 or postIndex < 0 or inStart > inEnd:
            return None
        
        root = TreeNode(postorder[postIndex])
        
        inIndex = 0
        
        for i in range(inEnd + 1):
            if inorder[i] == root.val:
                inIndex = i
                break
        
        root.right = self.buildTreeHelper(postIndex - 1, inIndex + 1, inEnd, inorder, postorder)
        root.left = self.buildTreeHelper(postIndex - (inEnd - inIndex) - 1, inStart, inIndex - 1, inorder, postorder)
        
        return root
