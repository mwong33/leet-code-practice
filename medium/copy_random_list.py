"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # O(n) time O(n) space
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        
        # {og node: copied node}
        index = {}
        
        copy = Node(1)
        pointer = head
        copy_pointer = copy
        
        while pointer != None:
            # Handle the next node
            if pointer in index:
                copy_pointer.next = index[pointer]
            else:
                copy_pointer.next = Node(pointer.val)
                index[pointer] = copy_pointer.next
            
            # Handle the next node's random
            if pointer.random != None and pointer.random in index:
                copy_pointer.next.random = index[pointer.random]
            elif pointer.random != None:
                copy_pointer.next.random = Node(pointer.random.val)
                index[pointer.random] = copy_pointer.next.random
            
            pointer = pointer.next
            copy_pointer = copy_pointer.next

        return copy.next
