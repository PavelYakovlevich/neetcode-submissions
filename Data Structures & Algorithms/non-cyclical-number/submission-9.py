class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.get_digits_sqr_sum(n)

        while slow != fast:
            fast = self.get_digits_sqr_sum(self.get_digits_sqr_sum(fast))
            slow = self.get_digits_sqr_sum(slow)
        
        return fast == 1
    
    def get_digits_sqr_sum(self, n: int) -> int:
        res = 0
        while n:
            res += (n % 10) ** 2
            n //= 10
        
        return res