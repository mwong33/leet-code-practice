# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time O(n) space
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Grab left subtree, convert that to pre-order linked list
        # Grab right subtree, convert that to pre-order linked list
        # Make left None and make right the left pre-order linked list
        # Attach the right pre-order LL to the right of the end of the left
        # pre-order LL
        self.convertTreeToPreOrderList(root)
        
    def convertTreeToPreOrderList(self, root):
        if root == None:
            return None
        
        if root.left == None and root.right == None:
            return root
        
        left_tail = self.convertTreeToPreOrderList(root.left)
        right_tail = self.convertTreeToPreOrderList(root.right)
        
        if left_tail != None and right_tail != None:
            right_head = root.right
            root.right = root.left
            root.left = None
            left_tail.right = right_head
            return right_tail
        elif left_tail != None:
            root.right = root.left
            root.left = None
            return left_tail
        else:
            root.left = None
            return right_tail
            
