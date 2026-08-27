class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = 1
        for x in range(1, len(nums) + 1):
            left = x
            for i in range(len(nums)):
                if left < 0:
                    break
                left -= int(nums[i] >= x)

            if not left:
                return x

        return -1
            
            