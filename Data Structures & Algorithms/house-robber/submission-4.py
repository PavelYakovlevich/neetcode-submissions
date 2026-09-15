class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 3)
        for i in range(len(nums) - 1, -1, -1):
            dp[i] = nums[i] + max(dp[i + 2], dp[i + 3])

        return max(dp[0], dp[1])