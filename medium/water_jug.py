class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0 or x == z or y == z or x + y == z:
            return True
        
        if x == 0 or y == 0:
            return False
        
        if z > x + y:
            return False
        
        print(self.greatestCommonDivisor(x,y))
        
        if z % self.greatestCommonDivisor(x,y) == 0:
            return True
        
        return False
    
    def greatestCommonDivisor(self, x, y):
        big = max(x,y)
        small = min(x,y)
        
        if small == 0:
            return big
        
        big = big%small
        
        return self.greatestCommonDivisor(big, small)
