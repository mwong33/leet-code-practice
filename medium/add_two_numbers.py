# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) space O(n) time
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output_number = 0
        
        l1_node = l1
        multiplier = 1
        
        while l1_node != None:
            output_number += (multiplier * l1_node.val)
            l1_node = l1_node.next
            multiplier *= 10
                    
        l2_node = l2
        multiplier = 1
        
        while l2_node != None:
            output_number += (multiplier * l2_node.val)
            l2_node = l2_node.next
            multiplier *= 10
                        
        output_list = ListNode(output_number%10)
        temp_pointer = output_list
        output_number = output_number//10
        
        while output_number > 0:
            temp_pointer.next = ListNode(output_number%10)
            temp_pointer = temp_pointer.next
            output_number = output_number//10
            
        return output_list
