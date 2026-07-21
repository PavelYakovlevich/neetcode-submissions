class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        
        ins, pos = 1, 2
        while pos < len(nums):
            if nums[pos] > nums[ins - 1]:
                ins += 1
                nums[ins] = nums[pos]
            pos += 1

        return ins + 1