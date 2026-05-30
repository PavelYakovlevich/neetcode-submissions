class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueNums = set(nums)

        nums.clear()

        nums.extend(uniqueNums)

        nums.sort()

        return len(uniqueNums)
