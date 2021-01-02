# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) time O(1) space where n is the length of the longer linked list
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # Loop through each list to get the length of both.
        # Iterate from the longer list the difference between the two lists (if there is a difference).
        # Iterate from both lists and check each node if they are the same until we reach None. 
        # Return True if any node is the same and if the loop is finished, return False.
        
        lenA = 0
        tempA = headA
        
        while tempA != None:
            lenA += 1
            tempA = tempA.next
        
        lenB = 0
        tempB = headB
        
        while tempB != None:
            lenB += 1
            tempB = tempB.next
            
        tempA = headA
        tempB = headB
        
        if lenA > lenB:
            diff = lenA - lenB
            while diff > 0:
                tempA = tempA.next
                diff -= 1
            
        elif lenB > lenA:
            diff = lenB - lenA
            
            while diff > 0:
                tempB = tempB.next
                diff -= 1
        
        while tempB != None:
            if tempB == tempA:
                return tempB
            
            tempB = tempB.next
            tempA = tempA.next
            
        return None
