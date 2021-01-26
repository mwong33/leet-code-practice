import heapq

class Solution:
    # Dictionary + Heap O(nlogk) time O(n + k) space
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        heap = []
        
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
                
        for number, count in nums_dict.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, number))
            else:
                if count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, number))
                    
        output = []
        
        while len(heap) > 0:
            output.append(heapq.heappop(heap)[1])
            
        return output
        
"""
[1, 1, 1, 2, 2, 3]

1. Dict = {1: 1}
2. Dict = {1: 2}
3. Dict = {1: 3}
4. Dict = {1: 3, 2: 1}
5. Dict = {1: 3, 2: 2}
6. Dict = {1: 3, 2: 2, 3: 1}

loop through keys

Insert (3, 1)
Insert (2, 2)

Pop em
"""
