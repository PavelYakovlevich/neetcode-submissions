class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([1])

        while n not in seen:
            seen.add(n)
            n = self.get_digits_sqr_sum(n)
        
        return n == 1
    
    def get_digits_sqr_sum(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n % 10) ** 2
            n //= 10
        
        return res