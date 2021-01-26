class Solution:
    # Heap O(nlogK) time O(n) space
    def kClosestHeap(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            if len(heap) < K:
                heapq.heappush(heap, (-1*self.distance(point), point))
            else:
                if self.distance(point) < (-1*heap[0][0]):
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-1*self.distance(point), point))
                    
        output = []
        while len(heap) > 0:
            output.append(heapq.heappop(heap)[1])
        
        return output
    
    def distance(self, point):
        return (point[0]**2 + point[1]**2)**0.5
        
"""
[[3, 3], [5, -1], [-2, 4]]

sqrt(18), sqrt(26), sqrt(8)
"""
    
    # Sorting and Dictionary - O(nlogn) time O(n) space
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_dict = {}
        distance_array = []
        
        for point in points:
            distance = (point[0]**2 + point[1]**2)**0.5
            distance_array.append(distance)
            
            if distance not in distance_dict:
                distance_dict[distance] = [point]
            else:
                distance_dict[distance].append(point)
            
        distance_array.sort()
        
        output = []
        index = 0
        
        while index < K:
            if len(distance_dict[distance_array[index]]) == 1:
                output.append(distance_dict[distance_array[index]][0])
                index += 1
            else:
                for point in distance_dict[distance_array[index]]:
                    output.append(point)
                    index += 1
        
        return output
    
    import heapq
