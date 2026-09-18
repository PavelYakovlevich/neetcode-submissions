class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        score = float('inf')
        k -= 1
        for i in range(len(nums) - k):
            score = min(score, nums[i + k] - nums[i])

        return score
