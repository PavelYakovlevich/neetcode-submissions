class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = {}
        
        def dfs(i):
            if i in cache: 
                return cache[i]
            if i >= len(nums) - 1:
                return 0

            jumps = float('inf')
            for j in range(nums[i], 0, -1):
                jumps = min(jumps, dfs(i + j))
            
            cache[(i)] = 1 + jumps
            return cache[(i)]
        
        return dfs(0)