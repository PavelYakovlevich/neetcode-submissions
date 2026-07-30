class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1

        cnt = Counter(s)

        res = 0
        for _, count in cnt.items():
            res += count if count % 2 == 0 else count - 1
        
        return res if res == len(s) else res + 1 