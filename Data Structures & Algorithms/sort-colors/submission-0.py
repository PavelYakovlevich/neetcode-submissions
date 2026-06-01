class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = [0] * 3

        for num in nums:
            count[num] += 1
        
        ins = 0
        for i in range(len(count)):
            for c in range(count[i]):
                nums[ins] = i
                ins += 1