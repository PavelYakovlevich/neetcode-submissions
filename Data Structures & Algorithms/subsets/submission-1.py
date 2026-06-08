class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for mask in range(0, pow(2, len(nums))):
            subset = []
            for i in range(len(nums)):
                if mask >> i & 1:
                    subset.append(nums[i])

            res.append(subset)
        
        return res