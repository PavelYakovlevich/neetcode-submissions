class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        seen = set()
        n = len(nums)
        for mask in range(2 << n):
            subset = [nums[i] for i in range(n) if (mask >> i) & 1 == 1]
            t = tuple(subset)

            if t not in seen:
                seen.add(t)
                res.append(subset)
        
        return res