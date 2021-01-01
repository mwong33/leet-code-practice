class Solution:
    # O(n^2) time O(n^2) space
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]
        
        output_list = [[1], [1,1]]
        index = 3
        
        while index <= numRows:
            last_row = output_list[len(output_list) - 1]
            new_row = []
            
            for i in range(len(last_row) - 1):
                new_row.append(last_row[i] + last_row[i + 1])
                    
            output_list.append([1] + new_row + [1])
            index += 1
        
        return output_list
