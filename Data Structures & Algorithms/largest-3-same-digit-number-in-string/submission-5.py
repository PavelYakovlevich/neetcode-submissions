class Solution:
    def largestGoodInteger(self, num: str) -> str:
        nums = [0] * len(num)
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                nums[int(num[i])] += 1
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i]:
                return ''.join([str(i)] * 3)

        return ''