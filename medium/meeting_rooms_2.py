import heapq

class Solution:
    # O(nlogn) time O(n) space
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        heapq.heappush(heap, intervals[0][1])
        room_count = 1
        
        for i in range(1, len(intervals)):
            if intervals[i][0] >= heap[0]:
                heapq.heappop(heap)
            else:
                room_count += 1
            heapq.heappush(heap, intervals[i][1])
        
        return room_count
    
"""
(1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)

1. R1: (1, 10) Heap: [10]
2. R1: (1, 10) R2: (2, 7) Heap: [7, 10]
3. R1: (1, 10) R2: (2, 7) R3: (3, 19) Heap: [7, 10, 19]
4. R1: (1, 10) R2: (8, 12) R3: (3, 19) Heap: [10, 12, 19]
5. R1: (10, 20) R2: (8, 12) R3: (3, 19) Heap: [12, 19, 20]
6. R1: (10, 20) R2: (8, 12) R3: (3, 19) R4: (11, 30) Heap: [12, 19, 20, 30]
"""
