class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_decreasing = is_increasing = True
        i = 1  
        while i < len(nums) and (is_increasing or is_decreasing):
            is_increasing = is_increasing and nums[i] <= nums[i - 1]
            is_decreasing = is_decreasing and nums[i] >= nums[i - 1]
            i += 1
            
        return is_increasing or is_decreasing