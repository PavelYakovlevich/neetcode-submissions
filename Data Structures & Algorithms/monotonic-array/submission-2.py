class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_decreasing = is_increasing = True

        for i in range(1, len(nums)):
            is_increasing = is_increasing and nums[i] <= nums[i - 1]
            is_decreasing = is_decreasing and nums[i] >= nums[i - 1]
            
        return is_increasing or is_decreasing