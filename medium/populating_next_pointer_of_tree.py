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
    def connectBFS(self, root: 'Node') -> 'Node':
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
    
    # DFS - O(n) time O(1) space
    def connectDFS(self, root: 'Node') -> 'Node':
        if root == None:
            return
        
        if root.left != None:
            # Setup the children
            root.left.next = root.right
            
        self.dfs(root.left)
        self.dfs(root.right)
        
        return root
    
    def dfs(self, root):
        if root == None:
            return
        
        # Check if you need to merge the middle
        if root.next != None and root.next.left != None:
            root.right.next = root.next.left
            
        # Merge your children
        if root.left != None:
            root.left.next = root.right
        
        self.dfs(root.left)
        self.dfs(root.right)
