from collections import deque

class Solution:
    # DFS O(V+E) time O(V + E) space
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if prerequisites == []:
            output = []
            for i in range(numCourses):
                output.append(i)
                
            return output
                
        # Convert prereqs to adjacency list
        adj_list = {}
        
        for prereq in prerequisites:
            if prereq[1] not in adj_list:
                adj_list[prereq[1]] = [prereq[0]]
            else:
                adj_list[prereq[1]].append(prereq[0])

        
        # 0 - unvisited, 1 - processing, 2 - done
        visited = [0] * numCourses         
        output = []
                                           
        for origin_class in range(numCourses):
            if visited[origin_class] == 2:
                continue
                                           
            if self.dfs(adj_list, origin_class, visited, output):
                return []
                                           
        return output[::-1]
                                         
    def dfs(self, adj_list, current_class, visited, output):
        if visited[current_class] == 2:
            return False
                                           
        if visited[current_class] == 1:
            return True
        
        visited[current_class] = 1
        
        if current_class in adj_list:
            while len(adj_list[current_class]) > 0:
                next_class = adj_list[current_class].pop()
                result = self.dfs(adj_list, next_class, visited, output)
                if result:
                    return True
            visited[current_class] = 2
            output.append(current_class)
            return False
        else:
            visited[current_class] = 2
            output.append(current_class)
            return False
