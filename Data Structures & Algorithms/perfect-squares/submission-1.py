class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        
        def dfs(remaining: int) -> int:
            if remaining == 0:
                return 0
                
            if remaining in cache:
                return cache[remaining]
            
            i = int(remaining ** 0.5)
            res = float('inf')

            while i >= 1:
                res = min(res, 1 + dfs(remaining - i ** 2))
                i -= 1

            cache[remaining] = res
            return res

        return dfs(n)