# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time O(1) space
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Step One: Get the length of the Linked List
        # Step Two: Iterate through the Linked List for length - n
        # Step Three: Remove the nth node
        # Step Four: Return the head
        
        length = 0
        temp = head
        
        while temp != None:
            length += 1
            temp = temp.next
                            
        if length - n == 0:
            head = head.next
        else:
            count = 1
            temp = head
            
            while count < length - n:
                temp = temp.next
                count += 1
            temp.next = temp.next.next
        
        return head
