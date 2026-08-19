class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = defaultdict(int)
        res = max_char_frequency = 0
        
        l = r = 0
        while max(l, r) < len(s):
            frequencies[s[r]] = 1 + frequencies[s[r]]
            max_char_frequency = max(max_char_frequency, frequencies[s[r]])

            if (r - l + 1) - max_char_frequency <= k:
                res = max(res, (r - l + 1))
            else:
                frequencies[s[l]] = frequencies[s[l]] - 1
                l += 1

            r += 1
        
        return res
