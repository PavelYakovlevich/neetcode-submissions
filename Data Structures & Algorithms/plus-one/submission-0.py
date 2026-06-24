class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = deque()
        remainder = 1
        for i in range(len(digits) - 1, -1, -1):
            res.appendleft((remainder + digits[i]) % 10)
            remainder = (remainder + digits[i]) // 10

        if remainder:
            res.appendleft(remainder)
            
        return list(res)