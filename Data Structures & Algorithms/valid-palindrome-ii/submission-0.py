class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        
        for skip_pos in range(len(s)):
            l, r = 0, len(s) - 1

            while l <= r:
                if l == skip_pos:
                    l += 1
                elif r == skip_pos:
                    r -= 1
                else:
                    if s[l] != s[r]:
                        break;
                    l += 1
                    r -= 1
            
            if l > r:
                return True
        
        return False