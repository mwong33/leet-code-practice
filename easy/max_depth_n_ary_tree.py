"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    # O(n) space O(n) time
    def maxDepth(self, root: 'Node') -> int:
        if root == None:
            return 0
        
        if root.children == None:
            return 1
        
        current_list = []
        next_list = []
        
        current_list.append(root)
        
        depth = 0
        
        while len(current_list) != 0:
            current_node = current_list.pop()
            
            # Add children
            for child in current_node.children:
                if child != None:
                    next_list.append(child)
                
            # Only add to depth when current list is empty
            if len(current_list) == 0:
                depth += 1
                current_list = next_list
                next_list = []
                
        return depth
