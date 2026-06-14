class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []

        border = lower
        for num in nums:
            if border != num:
                res.append([border, num - 1])
            border = num + 1

        if border <= upper:
            res.append([border, upper])

        return res