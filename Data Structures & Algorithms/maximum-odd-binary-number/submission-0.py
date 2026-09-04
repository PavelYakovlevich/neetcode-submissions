class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = 0
        for i in range(len(s)):
            ones_count += int(s[i] == '1')
        
        res = ['0'] * len(s)
        for i in range(0, ones_count - 1):
            res[i] = '1'
        
        if ones_count > 0:
            res[-1] = '1'
        
        return ''.join(res)