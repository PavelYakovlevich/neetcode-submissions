class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            nums[abs(num) - 1] *= -1
            if nums[abs(num) - 1] > 0:
                res.append(abs(num))

        return res