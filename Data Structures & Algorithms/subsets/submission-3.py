class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for mask in range(2 ** len(nums)):
            subset = [nums[i] for i in range(len(nums)) if ((mask >> i) & 1) == 1]

            res.append(subset)

        return res