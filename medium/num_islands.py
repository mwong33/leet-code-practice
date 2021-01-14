# O(n*m) time and O(n*m) space
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1) Visit each node
        # 2) If the node is 0 ignore it
        # 3) If it is 1 AND not visited, DFS it and add all 1 connected nodes into our visited. 
        #    THEN Increment our island_count by 1
        # 4) Return our island_count
        visited = set()
        island_count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    self.dfs(row, col, grid, visited)
                    island_count += 1
                
        return island_count
    
    def dfs(self, row, col, grid, visited):
        # Add this coordinate to visited
        visited.add((row, col))
        
        # Visit all 1 neighbors that have not been visited
        # top
        if row != 0 and grid[row-1][col] == "1" and (row-1, col) not in visited:
            self.dfs(row-1, col, grid, visited)
        
        # bottom
        if row != len(grid) - 1 and grid[row+1][col] == "1" and (row+1, col) not in visited:
            self.dfs(row+1, col, grid, visited)
            
        # left
        if col != 0 and grid[row][col-1] == "1" and (row, col-1) not in visited:
            self.dfs(row, col-1, grid, visited)
        
        # right
        if col != len(grid[0]) - 1 and grid[row][col+1] == "1" and (row, col+1) not in visited:
            self.dfs(row, col+1, grid, visited)
