from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    # BFS - O(n) time O(m) space where n is the number of nodes. m is the number of leaf nodes
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return
        
        current_level = deque([root])
        next_level = deque([])
                
        while len(current_level) != 0:
            current_node = current_level.popleft()
            
            if current_node.left != None:
                if len(next_level) != 0:
                    next_level[-1].next = current_node.left
                next_level.append(current_node.left)
                
            if current_node.right != None:
                if len(next_level) != 0:
                    next_level[-1].next = current_node.right
                next_level.append(current_node.right)
                
                
            if len(current_level) == 0:
                current_level = next_level
                next_level = deque([])
                
        return root
