class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1
        inc_len = dec_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1
            elif nums[i] < nums[i - 1]:
                dec_len += 1
                inc_len = 1
            else:
                inc_len = dec_len = 1
            
            res = max(res, max(inc_len, dec_len))
        
        return res