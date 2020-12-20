# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # O(n) space O(n) time
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y:
            return False
        
        current_list = []
        next_list = []
        level_dictionary = {}
        current_level = 0
        
        current_list.append(root)
        
        while len(current_list) != 0:
            current_node = current_list.pop()
            
            # Add children to the next_list and level_dictionary
            if current_node.left != None:
                next_list.append(current_node.left)
                level_dictionary[current_node.left.val] = current_level + 1
                
            if current_node.right != None:
                next_list.append(current_node.right)
                level_dictionary[current_node.right.val] = current_level + 1
                
            if current_node.right != None and current_node.left != None:
                if current_node.right.val == x and current_node.left.val == y:
                    return False
                elif current_node.right.val == y and current_node.left.val == x:
                    return False
                
            if len(current_list) == 0:
                current_level += 1
                current_list = next_list
                next_list = []
                
        return level_dictionary[x] == level_dictionary[y]
