class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(i: int, acc: int) -> int:
            if (i, acc) in cache:
                return cache[(i, acc)]
                
            if i == len(nums):
                return (int)(acc == target)
            
            add = dfs(i + 1, acc + nums[i])
            substract = dfs(i + 1, acc - nums[i])
            
            cache[(i, acc)] = add + substract

            return cache[(i, acc)]
        
        return dfs(0, 0)