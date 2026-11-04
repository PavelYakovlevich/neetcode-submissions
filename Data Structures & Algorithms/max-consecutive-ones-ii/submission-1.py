class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        prev_zero = -1
        left = 0
        res = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                left = prev_zero + 1
                prev_zero = right
            res = max(res, right - left + 1)
        return res