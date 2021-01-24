class Solution:
    # O(nlogn) time O(n) space if you count our output array as extra memory
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged_intervals = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] > merged_intervals[-1][1]:
                merged_intervals.append(intervals[i])
            elif intervals[i][1] > merged_intervals[-1][1]:
                merged_intervals[-1] = [merged_intervals[-1][0], intervals[i][1]]
        
        return merged_intervals

"""
(1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)

1. [[1, 10]]
2. [[1, 10]]
3. [[1, 19]]
4. [[1, 20]]
5. [[1, 30]]
"""
