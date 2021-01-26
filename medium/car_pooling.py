import heapq

class Solution:
    # O(nlogn) time O(n) space
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort the trips based on start time
        trips.sort(key=lambda trip: trip[1])

        heap = []
        heapq.heappush(heap, [trips[0][2], trips[0][0]])
        capacity -= trips[0][0]
        
        for i in range(1, len(trips)):
            if trips[i][1] >= heap[0][0]:
                while len(heap) != 0 and heap[0][0] <= trips[i][1]:
                    removed = heapq.heappop(heap)
                    capacity += removed[1]
            capacity -= trips[i][0]
            
            if capacity < 0:
                return False
            
            heapq.heappush(heap, [trips[i][2], trips[i][0]])
        
        return True
"""
Heap: [[End Time, Passenger Size]]

[[3, 2, 7], [8, 3, 9], [3, 7, 9]], 11

1. Capacity = 8, Heap: [[7, 3]]
2. Capacity = 0, Heap: [[7, 3], [9, 8]] 
3. Capacity = 0, Heap: [[9, 8], [9, 3]]

----------------------------------------------

[[3, 2, 8], [4, 4, 6], [10, 8, 9]], 11

1. Capacity = 8, Heap: [[8, 3]]
2. Capacity = 4, Heap: [[6, 4], [8, 3]]
3. Capacity = 1, Heap: [[9, 10]]
"""
