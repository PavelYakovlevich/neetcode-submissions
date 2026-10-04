class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negatives = 0
        for num in nums:
            if not num:
                return 0
            negatives += int(num < 0)
        
        return -1 if negatives & 1 == 1 else 1