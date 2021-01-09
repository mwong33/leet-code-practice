# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time O(h) space for output where h is the height of the tree
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        # BFS and only add the right most node to our output array
        if root == None:
            return []
        
        output = [root.val]
        
        current_level = [root]
        next_level = []
        
        while len(current_level) != 0:
            current_node = current_level.pop(0) # would be constant time if we used a proper queue
            
            # Add children to next_level
            if current_node.left != None:
                next_level.append(current_node.left)
            if current_node.right != None:
                next_level.append(current_node.right)
                
            if len(current_level) == 0:
                current_level = next_level
                next_level = []
                if len(current_level) != 0:
                    output.append(current_level[-1].val)
        
        return output
