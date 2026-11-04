class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1] - 1
            if diff >= k:
                return nums[i - 1] + k
            k -= diff
        
        return nums[-1] + k