class Solution:
    # O(n) time O(n) space
    def tribonacci(self, n: int) -> int:
        return self.tribonacciRecursion(n, {})
    
    def tribonacciRecursion(self, n, cache):
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 1
        
        if n in cache:
            return cache[n]
        else:
            cache[n] = self.tribonacciRecursion(n-3, cache) + self.tribonacciRecursion(n-2, cache) + self.tribonacciRecursion(n-1, cache)
            
        return cache[n]
