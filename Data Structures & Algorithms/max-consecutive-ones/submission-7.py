class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for num in nums:
            count = count + 1 if num else 0
            res = max(res, count)

        return res
