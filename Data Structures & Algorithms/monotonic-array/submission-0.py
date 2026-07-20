class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        is_decreasing = is_increasing = True

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] < nums[i - 1]:
                is_increasing = False
            if nums[i] > nums[i - 1]:
                is_decreasing = False
            
        return is_increasing or is_decreasing