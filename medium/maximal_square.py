class Solution:
    # O(m*n) space O(1) time
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_square_side = 0
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    if row == 0:
                        if max_square_side < 1:
                            max_square_side = 1
                        continue
                    if col == 0:
                        if max_square_side < 1:
                            max_square_side = 1
                        continue
                        
                    top = int(matrix[row-1][col])
                    left = int(matrix[row][col-1])
                    diagonal = int(matrix[row-1][col-1])
                    
                    minimum = min(top, left, diagonal)
                    matrix[row][col] = str(minimum + 1)
                                        
                    if int(matrix[row][col]) > max_square_side:
                        max_square_side = int(matrix[row][col])
                        
        return max_square_side * max_square_side
