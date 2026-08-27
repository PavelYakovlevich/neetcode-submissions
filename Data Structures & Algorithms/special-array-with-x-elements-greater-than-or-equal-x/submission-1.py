class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()

        L = 0
        for x in range(1, len(nums) + 1):
            while L < len(nums) and x > nums[L]:
                L += 1
            
            if len(nums) - L == x:
                return x
        
        return -1
            