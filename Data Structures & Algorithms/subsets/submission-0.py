class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for i in range(0, pow(2, len(nums))):
            subset = []
            for j in range(len(nums)):
                if i >> j & 1:
                    subset.append(nums[j])

            res.append(subset)
        
        return res