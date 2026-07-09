class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}

        def dfs(cost: List[int], i: int) -> int:
            if i >= len(cost):
                return 0
            
            next = 0
            if i + 1 in cache:
                next = cache[i + 1]
            else:
                next = dfs(cost, i + 1)
                cache[i + 1] = next

            double = 0
            if i + 2 in cache:
                double = cache[i + 2]
            else:
                double = dfs(cost, i + 2)
                cache[i + 2] = double
            
            return cost[i] + min(next, double)
        
        return min(dfs(cost, 0), dfs(cost, 1))