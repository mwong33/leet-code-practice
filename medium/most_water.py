class Solution:
    # O(n) time O(1) space
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        
        max_volume = -1
        
        while start < end:
            current_volume = min(height[start],height[end]) * (end - start)
            if current_volume > max_volume:
                max_volume = current_volume
            
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
                
        return max_volume
