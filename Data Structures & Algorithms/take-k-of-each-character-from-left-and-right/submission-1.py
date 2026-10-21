class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        if min(count) < k:
            return -1
        
        res = 0
        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('a')] -= 1
            while min(count) < k:
                count[ord(s[l]) - ord('a')] += 1
                l += 1
            
            res = max(res, r - l + 1)
        return len(s) - res
