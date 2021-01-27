import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Heap - O(nklog(nk)) time O(nk) space
    # n - no. of lists, k - average length of list
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:        
        heap = []
        
        for head in lists:
            temp = head
            while temp != None:
                heapq.heappush(heap, temp.val)
                temp = temp.next
                
        if len(heap) == 0:
            return None
            
        output = ListNode()
        temp = output
        
        while len(heap) != 0:
            temp.val = heapq.heappop(heap)
            
            if len(heap) != 0:
                temp.next = ListNode()
                temp = temp.next
        
        return output
