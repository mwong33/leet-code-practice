import heapq

class Solution:
    # O(nlogn) time O(1) space
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert list to a max heap using heapq and -1 hack
        # Pull the top two numbers
        # Get the difference
        # Check if heap is empty if it is return the difference, 
        # otherwise insert the difference back into the max heap
        
        if len(stones) == 1:
            return stones[0]
        
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
            
        heapq.heapify(stones)
        
        while len(stones) > 1:
            heaviest_stone = -1* heapq.heappop(stones)
            second_heaviest_stone = -1 * heapq.heappop(stones)
            
            difference = heaviest_stone - second_heaviest_stone
            
            if difference != 0:
                heapq.heappush(stones, -1 * difference)
                
        if len(stones) == 0:
            return 0
        else:
            return -1 * heapq.heappop(stones)
