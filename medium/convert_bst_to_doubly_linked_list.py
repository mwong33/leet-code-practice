"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# O(n) time O(n) space
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        
        # Step One: Convert Tree to inorder array
        inorder_array = self.convertToArray(root)
        
        # Step Two: Create the head
        head = Node(inorder_array[0])
        
        if len(inorder_array) == 1:
            head.left = head
            head.right = head
            return head
        
        pointer = head
        
        for index in range(1, len(inorder_array)):
            next_node_value = inorder_array[index]
            temp = pointer
            pointer.right = Node(next_node_value)
            pointer = pointer.right
            pointer.left = temp
            
        pointer.right = head
        head.left = pointer
        
        return head
        
    def convertToArray(self, root):
        if root == None:
            return []
        
        left_array = self.convertToArray(root.left)
        right_array = self.convertToArray(root.right)
        
        return left_array + [root.val] + right_array
