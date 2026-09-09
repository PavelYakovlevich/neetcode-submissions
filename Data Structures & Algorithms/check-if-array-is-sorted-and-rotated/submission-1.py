class Solution:
    def check(self, nums: List[int]) -> bool:
        split_pos = len(nums)
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                split_pos = i
                break        
        
        for i in range(1, len(nums)):
            if i == split_pos:
                continue
            if nums[i] < nums[i - 1]:
                return False
        
        if split_pos < len(nums) and nums[-1] > nums[0]:
            return False

        return True