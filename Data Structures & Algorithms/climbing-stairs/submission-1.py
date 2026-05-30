class Solution:
    def __init__(self):
        self.cache = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return max(0, n)

        cached_n_2 = self.cache.get(n - 2, 0)
        cached_n_1 = self.cache.get(n - 1, 0)

        n2 = cached_n_2 if cached_n_2 != 0 else self.climbStairs(n - 2) 
        n1 = cached_n_1 if cached_n_1 != 0 else self.climbStairs(n - 1) 

        if not cached_n_2:
            self.cache[n - 2] = n2

        if not cached_n_1:
            self.cache[n - 1] = n1
        
        return n2 + n1