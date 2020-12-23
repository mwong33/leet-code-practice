class Solution:
    # O(n) time O(1) space
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Greedy Algorithm
        # Iterate through the flowerbed
        # 1) Check if current plot is 0 if it is not just increment to the next plot
        # 2) If it is 0 check plot in front to see if it is 0 and check plot after to see if it is 0
        # 3) If the checks above are true, decrement n and plant the plot with a flower (change it to 1)
        # 4) If the checks above are false increment to the next plot
        # 5) Check is n is 0 if it is 0 return True otherwise return False
        
        if n == 0:
            return True
        
        if len(flowerbed) == 1:
            if flowerbed[0] == 1:
                return False
            elif n > 1:
                return False
            else:
                return True
        
        flowers_remaining = n
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i > 0 and i < len(flowerbed) - 1:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        flowers_remaining -= 1
                elif i == 0:
                    if flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        flowers_remaining -= 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        flowers_remaining -= 1
            
            if flowers_remaining == 0:
                return True
        
        return False
