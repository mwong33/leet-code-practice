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

    # O(n) time O(1) space iterative solution
    def tribonacciIterative(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 1
        
        if n == 2:
            return 1
        
        one_behind = 1
        two_behind = 1
        three_behind = 0
        
        for i in range(4,n+1):
            old_one_behind = one_behind
            old_two_behind = two_behind
            one_behind = one_behind + two_behind + three_behind
            two_behind = old_one_behind
            three_behind = old_two_behind
            
        
        return one_behind + two_behind + three_behind
