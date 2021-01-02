# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) time O(1) space
    def hasCycleFlag(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        while head != None:
            if head.val == "x":
                return True
            
            head.val = "x"
            head = head.next
            
        return False
    
    # O(n) time O(1) space
    def hasCycleTwoPointers(self, head: ListNode) -> bool:
        if head == None:
            return False
        
        if head.next == None:
            return False
        
        if head.next.next == None:
            return False
        
        slow_pointer = head.next
        fast_pointer = head.next.next
        
        while slow_pointer != None:
            if slow_pointer == fast_pointer:
                return True
            
            slow_pointer = slow_pointer.next
            
            if fast_pointer.next == None:
                return False
            if fast_pointer.next.next == None:
                return False
            
            fast_pointer = fast_pointer.next.next
            
        return False
