class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return max(0, n)

        cached_n = self.cache.get(n, 0)
        if cached_n:
            return cached_n

        n2 = self.climbStairs(n - 2) 
        n1 = self.climbStairs(n - 1) 

        self.cache[n] = n2 + n1
        
        return self.cache[n]