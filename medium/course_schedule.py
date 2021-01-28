class Solution:
    # O(V+E) time O(V+E) space
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Convert data to adjacency list
        adj_list = {}
        
        for pair in prerequisites:
            if pair[1] not in adj_list:
                adj_list[pair[1]] = [pair[0]]
            else:
                adj_list[pair[1]].append(pair[0])
         
        # 0 - Unvisited, 1 - Processed, 2 - Processing
        visited = [0] * numCourses
        
        for point in range(numCourses):
            if point not in adj_list:
                continue
            if self.findCycle(adj_list, point, visited):
                return False
            
        return True
            
    def findCycle(self, adj_list, point, visited):
        if visited[point] == 1:
            return False
        if visited[point] == 2:
            return True
        
        visited[point] = 2
        
        if point not in adj_list:
            visited[point] = 1
            return False
        else:
            while len(adj_list[point]) != 0:
                next_point = adj_list[point].pop()
                result = self.findCycle(adj_list, next_point, visited)
                if result:
                    return True
                
            visited[point] = 1
            return False
