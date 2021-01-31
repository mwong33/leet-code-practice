class Solution:
    # O(N * 3^L) and O(L)
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board, word, row, col, 0, set()):
                        return True
                
        return False
    
    def dfs(self, board, word, row, col, index, visited):        
        # Edge Cases
        if row < 0 or col < 0 or row > len(board) - 1 or col > len(board[0]) - 1:
            return False
        
        # Base Cases
        if word[index] != board[row][col]:
            return False
        if index == len(word) - 1:
            return True
        
        visited.add((row, col))
        
        # DFS
        for dx, dy in [(1,0), (-1,0), (0, 1), (0, -1)]:
            nx = col + dx
            ny = row + dy
            
            if (ny, nx) not in visited:
                if self.dfs(board, word, ny, nx, index+1, visited):
                    return True
                        
        visited.remove((row, col))
        
        return False
