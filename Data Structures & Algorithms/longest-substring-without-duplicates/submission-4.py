class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        l = r = 0

        while max(l, r) < len(s):
            if s[r] in window:
                res = max(res, len(window))
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                
            window.add(s[r])
            r += 1
        
        return max(res, len(window))