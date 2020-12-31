# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(m) time O(m+n) space where m is the size of the larger list and n is the smaller
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        
        l1_current = l1
        l2_current = l2
        
        combined_list = ListNode()
        temp_pointer = combined_list
        
        while l1_current or l2_current:
            if l1_current == None:
                temp_pointer.next = ListNode(l2_current.val)
                l2_current = l2_current.next
            elif l2_current == None:
                temp_pointer.next = ListNode(l1_current.val)
                l1_current = l1_current.next
            else:
                temp_pointer.next = ListNode(min(l1_current.val, l2_current.val))
                
                if l1_current.val < l2_current.val:
                    l1_current = l1_current.next
                else:
                    l2_current = l2_current.next
            
            temp_pointer = temp_pointer.next
                    
        return combined_list.next
