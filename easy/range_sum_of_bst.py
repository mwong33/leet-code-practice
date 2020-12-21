# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) time O(n) space
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        current_list = [root]
        next_list = []
        range_sum = 0
                
        while len(current_list) != 0:
            current_node = current_list.pop()
            
            if current_node.val <= high and current_node.val >= low:
                range_sum += current_node.val
                
            if current_node.left != None and current_node.val > low:
                next_list.append(current_node.left)
                
            if current_node.right != None and current_node.val < high:
                next_list.append(current_node.right)
                
            if len(current_list) == 0:
                current_list = next_list
                next_list = []
                
        return range_sum
    
    # O(n) time O(n) space recursive solution
    def rangeSumBSTRecursive(self, root: TreeNode, low: int, high: int) -> int:
        if root == None:
            return 0
        
        range_sum = 0
        # Check current val
        if root.val <= high and root.val >= low:
            range_sum += root.val
            
        # Add left subtree
        if root.left != None and root.val > low:
            range_sum += self.rangeSumBST(root.left, low, high)
        
        # Add right subtree
        if root.right != None and root.val < high:
            range_sum += self.rangeSumBST(root.right, low, high)
            
        return range_sum
