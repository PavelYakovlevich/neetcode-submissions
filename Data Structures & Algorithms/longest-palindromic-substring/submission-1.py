class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        res_L = res_R = 0
        for i in range(len(s)):
            L, R = i, i

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
            
            if (R - 1) - (L + 1) > res_R - res_L:
                res_L, res_R = L + 1, R - 1
        
        for i in range(len(s)):
            L, R = i, i + 1

            while L >= 0 and R < len(s) and s[L] == s[R]:
                L -= 1
                R += 1
                    
            if (R - 1) - (L + 1) > res_R - res_L:
                res_L, res_R = L + 1, R - 1

        return s[res_L:res_R + 1]