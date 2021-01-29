from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    # O(V + E) time O(V) space
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        if node.neighbors == []:
            return Node(node.val)
        
        # BFS Tools
        clone_dict = {}
        visited = set()
        queue = deque([])
        
        # Create the clone head
        clone = Node()
        clone.val = node.val
        
        # Add the clone to the clone dict and the node head to visited
        clone_dict[clone.val] = clone
        visited.add(node)
        
        # Add the neghbors
        for neighbor in node.neighbors:
            neighbor_copy = Node(neighbor.val)
            clone.neighbors.append(neighbor_copy)
            clone_dict[neighbor.val] = neighbor_copy
            queue.append(neighbor)
        
        # BFS
        while len(queue) != 0:
            new_node = queue.popleft()
            
            if new_node in visited:
                continue
            
            clone_node = clone_dict[new_node.val]
            visited.add(new_node)
            
            for neighbor in new_node.neighbors:
                if neighbor.val in clone_dict:
                    clone_node.neighbors.append(clone_dict[neighbor.val])
                else:
                    neighbor_copy = Node(neighbor.val)
                    clone_node.neighbors.append(neighbor_copy)
                    clone_dict[neighbor.val] = neighbor_copy
                
                if neighbor not in visited:
                    queue.append(neighbor)
                                        
        return clone
