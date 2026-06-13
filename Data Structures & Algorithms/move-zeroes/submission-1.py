class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        ins = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[ins] = nums[ins], nums[i]
                ins += 1