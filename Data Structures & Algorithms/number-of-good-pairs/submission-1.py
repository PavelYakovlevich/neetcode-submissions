class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 0
        for _, count in cnt.items():
            res += count * (count - 1) // 2
        return res