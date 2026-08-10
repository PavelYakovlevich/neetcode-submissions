class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        res = 0
        l = r = 0

        while r < len(s):
            if s[r] in window:
                while s[r] in window:
                    window.remove(s[l])
                    l += 1
                
            window.add(s[r])
            res = max(res, len(window))
            r += 1
        
        return res