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
