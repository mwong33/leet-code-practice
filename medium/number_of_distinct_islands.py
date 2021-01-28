class Solution:
    # O(n) time O(n) space
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        island_list_of_lists = []
        cache = set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in cache:
                    island2 = self.dfs(row, col, grid, cache)
                    
                    if len(island2) != 0:
                        add = True
                        for island1 in island_list_of_lists:
                            if self.compareIslands(island1, island2):
                                add = False
                                break
                            
                        if add:
                            island_list_of_lists.append(island2)
                        
        return len(island_list_of_lists)
        
        
    def dfs(self, row, col, grid, cache):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return []
        
        if (row, col) in cache:
            return []
        
        if grid[row][col] != 1:
            return []
        
        cache.add((row, col))
        
        # Top
        top = self.dfs(row-1, col, grid, cache)
        # Left
        left = self.dfs(row, col-1, grid, cache)
        # Right
        right = self.dfs(row, col+1, grid, cache)
        # Bottom
        bottom = self.dfs(row+1, col, grid, cache)
        
        return [(row, col)] + top + left + right + bottom
        
    def compareIslands(self, island1, island2):
        if len(island1) != len(island2):
            return False
        
        row_d = island2[0][0] - island1[0][0]
        col_d = island2[0][1] - island1[0][1]
        
        for index in range(len(island1)):
            translated = (island1[index][0] + row_d, island1[index][1] + col_d)
            
            if translated != island2[index]:
                return False
        
        return True
        
"""
DFS To find islands

Store each island as a list of tuples
compare the list with every other list
if it matches any don't add to island list of lists
if it doesn't match any, add it to our island list of lists
return the length of our list of lists
"""
