class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = {}

        def dfs(pos: int) -> bool:
            if pos in cache:
                return cache[pos]
                
            if pos >= len(nums) - 1:
                return pos == len(nums) - 1

            can_reach_end = False
            for jump in range(nums[pos], 0, -1):
                can_reach_end = can_reach_end or dfs(pos + jump)

            cache[pos] = can_reach_end
            return can_reach_end

        return dfs(0)
