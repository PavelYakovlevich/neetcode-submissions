class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)

        res = []
        for num, count in cnt.items():
            if count > 1:
                res.append(num)

        return res
