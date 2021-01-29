class Solution:
    # DFS 
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = self.dfs(graph, 0)

        for index in range(len(result)):
            result[index] = result[index][::-1]
    
        return result
    
    def dfs(self, graph, current_node):
        # Base Case
        if current_node == len(graph) - 1:
            return [[len(graph) - 1]]
        
        result = []
        
        index = 0
        for neighbor in graph[current_node]:
            neighbor_result = self.dfs(graph, neighbor)
            
            for index in range(len(neighbor_result)):
                neighbor_result[index].append(current_node)
            
            result += neighbor_result

        return result

"""
Start with node 0

DFS each of node 0's neighbors

Each of node 0's neighbors will explore thei rneighbors till we reach the last node recursively

bubble up a list of lists (which will be reversed at first)

"""
