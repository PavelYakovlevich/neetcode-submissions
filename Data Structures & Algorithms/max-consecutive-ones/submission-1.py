class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        pos = 0

        for i in range(len(nums)):
            if not nums[i]:
                res = max(res, i - pos)
                pos = i + 1

        if pos < len(nums):
            res = max(res, len(nums) - pos)

        return res
