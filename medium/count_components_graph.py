class Solution:
    # O(V + E) time O(V + E) space
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Make adj_list
        adj_list = [[] for _ in range(n)]
        
        for pair in edges:
            adj_list[pair[0]].append(pair[1])
            adj_list[pair[1]].append(pair[0])
            
        visited = set()
        output = 0
        
        for origin in range(n):
            if origin in visited:
                continue
                
            self.dfs(adj_list, origin, visited)
            output += 1
        
        return output
    
    def dfs(self, adj_list, origin, visited):        
        visited.add(origin)
        
        for neighbor in adj_list[origin]:
            if neighbor not in visited:
                self.dfs(adj_list, neighbor, visited)
            
        
                
