class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        for mask in range(2**n):
            subset = [nums[j] for j in range(n) if mask >> j & 1]
            res.append(subset)
        return res