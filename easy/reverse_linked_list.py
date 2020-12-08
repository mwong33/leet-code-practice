# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) space O(n) time
    def reverseListIterativeSolution(self, head: ListNode) -> ListNode:
        reversed_list = None
        
        iterate = True
        curr_node = head
        
        while iterate:
            if curr_node != None:
                temp_pointer = reversed_list
                reversed_list = ListNode(curr_node.val)
                reversed_list.next = temp_pointer
                curr_node = curr_node.next
            else:
                iterate = False
                
        return reversed_list
    
    # O(n) space O(n) time
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseListRecursion(head, None)
    
    def reverseListRecursion(self, head: ListNode, reverse_head: ListNode):
        if head == None:
            return reverse_head
        
        temp = reverse_head
        reverse_head = ListNode(head.val)
        reverse_head.next = temp
        return self.reverseListRecursion(head.next, reverse_head)
