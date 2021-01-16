class Solution:
    # Top Down Memo - O(N*N*K) time O(N*N*K) space
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:        
        return self.knightProbabilityMemo(N, K, r, c, 0, {})
    
    def knightProbabilityMemo(self, grid_size, total_moves, row, col, move_count, cache):
        if (row, col, move_count) in cache:
            return cache[(row, col, move_count)]
        
        # Base Cases
        if move_count == total_moves:
            return 1
        
        # Get Number of Options for current position
        valid_positions = self.getValidMovesList(grid_size, row, col)
        
        # Try all valid options and get their probabilites to stay on board
        probability = 0
        
        for new_position in valid_positions:
            probability += (1/8) * self.knightProbabilityMemo(grid_size, total_moves, new_position[0], new_position[1], move_count+1, cache)
        
        cache[(row, col, move_count)] = probability
        return probability
        
        
    def getValidMovesList(self, grid_size, x, y):
        valid_positions = []
        
        for dx, dy in [(1,2), (-1,2), (-1,-2), (1,-2), (2,1), (-2,1), (2,-1), (-2,-1)]:
            nx, ny = x + dx, y + dy
            # Check if we are out of bounds
            if nx < 0 or ny < 0 or nx >= grid_size or ny >= grid_size:
                continue
            valid_positions.append((nx, ny))
        
        return valid_positions
