# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(h) space
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            return [root.val]
        
        leaves = self.getLeaves(root)
        left_nodes = self.getLeftNodes(root.left)
        right_nodes = self.getRightNodes(root.right)
        
        return [root.val] + left_nodes + leaves + right_nodes
    
    def getLeaves(self, root):
        # Base Case
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            return [root.val]
        
        left_result = self.getLeaves(root.left)
        right_result = self.getLeaves(root.right)
        
        return left_result + right_result
    
    def getLeftNodes(self, root):
        # Base Case
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            return []
        
        advance = None
        if root.left != None:
            advance = self.getLeftNodes(root.left)
        else:
            advance = self.getLeftNodes(root.right)
            
        return [root.val] + advance
        
    def getRightNodes(self, root):
        # Base Case
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            return []
        
        advance = None
        if root.right != None:
            advance = self.getRightNodes(root.right)
        else:
            advance = self.getRightNodes(root.left)
        
        return advance + [root.val]
    
"""
Step One:

Get All Leaf Nodes

Step Two:

Get all left most nodes that are not leaves

Get all right most nodes that are not leaves

Step Three:

Combine Root + Left Most Nodes + Leaf Nodes + Right Nodes  (reversed)

"""
