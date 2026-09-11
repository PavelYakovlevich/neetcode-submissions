class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        candidate = 1
        while candidate ** 2 < num:
            candidate += 1
        
        return candidate ** 2 == num