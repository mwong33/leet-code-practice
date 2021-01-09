class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z == 0 or x == z or y == z or x + y == z:
            return True
        
        if z > x + y:
            return False
        
        if z % gcd(x,y) == 0:
            return True
        
        return False
