class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_special = True
        for i in range(0, len(nums) - 1, 2):
            is_special = is_special and nums[i] % 2 == 0 and nums[i + 1] % 2 != 0
        
        return is_special