# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time O(n) space
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # We could use DFS in the form of two arrays
        # current_level holds nodes on the level we are looking at
        # next_level holds the nodes on the next level
        # before we move on to the next_level we can add our next_level values to the output array
        # keep a boolean to keep track if we need to reverse the next_level values array or not before adding it to the output array
        if root == None:
            return None
        
        flip = True
        output_array = [[root.val]]
        
        current_level = [root]
        next_level = []
        next_level_values = []
        
        while len(current_level) != 0:
            current_node = current_level.pop(0) # If we used a proper queue for this implementation this would be O(1) time
            
            # Add the children
            if current_node.left != None:
                next_level.append(current_node.left)
                next_level_values.append(current_node.left.val)
            if current_node.right != None:
                next_level.append(current_node.right)
                next_level_values.append(current_node.right.val)
                
            if len(current_level) == 0:
                if len(next_level_values) != 0:
                    if flip:
                        flip = False
                        output_array.append(next_level_values[::-1])
                    else:
                        flip = True
                        output_array.append(next_level_values)
                
                current_level = next_level
                next_level = []
                next_level_values = []
                
        return output_array
