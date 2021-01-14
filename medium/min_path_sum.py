class Solution:
    # O(n*m) time O(n*m) space if you count the grid we are using as extra memory otherwise O(1) space (Bottom Up Table)
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Loop through each element from top to bottom left to right.
        # For the element we are one, try to calculate the shortest path to that element 
        # and replace the value with that shortest path value.
        # Do this by analyzing the left and top neighbors. Add the smaller neighbor to the value of that element.
        # Repeat this process for all elements.
        # Return the last element on the last row.
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                # Only check the left element
                if row == 0:
                    grid[row][col] = grid[row][col] + grid[row][col-1]
                # Only check the top element
                elif col == 0:
                    grid[row][col] = grid[row][col] + grid[row-1][col]
                # Check both the left and top element
                else:
                    left_option = grid[row][col-1]
                    top_option = grid[row-1][col]
                    
                    grid[row][col] = grid[row][col] + min(left_option, top_option)
        
        return grid[-1][-1]

"""
Bottom Up

1 3 1      1 4 5
1 5 1      2 7 6 
4 2 1      6 8 7

1 2 3      1 3 6
4 5 6      5 8 12

"""
