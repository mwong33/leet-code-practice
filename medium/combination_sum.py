class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def search(target, candidates, current_sum, start, carrier):
            if current_sum == target:
                copy = carrier.copy()
                output.append(copy)
            if current_sum > target:
                return
            
            for index in range(start, len(candidates)):
                carrier.append(candidates[index])
                search(target, candidates, current_sum+candidates[index], index, carrier)
                carrier.pop()
                
        search(target, candidates, 0, 0, [])
        
        return output
