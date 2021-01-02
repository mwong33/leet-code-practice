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
