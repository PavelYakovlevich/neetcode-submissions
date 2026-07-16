class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = acc = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                acc = 0
            
            acc += nums[i]
            res = max(res, acc)
        
        return res
