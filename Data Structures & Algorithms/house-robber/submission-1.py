class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(nums, i, cache):
            if i >= len(nums):
                return 0

            t1 = 0
            if (i + 1) in cache:
                t1 = cache[i + 1]
            else:
                t1 = dfs(nums, i + 1, cache)
                cache[i + 1] = t1
            
            t2 = 0
            if (i + 2) in cache:
                t2 = cache[i + 2]
            else:
                t2 = dfs(nums, i + 2, cache)
                cache[i + 2] = t2

            return max(nums[i] + t2, t1)
        return dfs(nums, 0, {})