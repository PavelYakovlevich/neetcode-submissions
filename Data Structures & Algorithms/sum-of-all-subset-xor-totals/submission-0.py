class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_total = 0
        for num in nums:
            or_total |= num 
            
        return or_total << (len(nums) - 1)