class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for key, value in counter.items():
            if value >= len(nums) // 2:
                return key