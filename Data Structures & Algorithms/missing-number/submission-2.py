class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        max_num = 0

        for num in nums:
            s.add(num)
            max_num = max(num, max_num)
        
        i = 0
        while i <= max_num:
            if not i in s:
                return i
            i += 1
        return i


