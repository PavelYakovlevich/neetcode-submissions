class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        cnt = Counter(t)
        matches = l = r = 0
        res_start, res_len = -1, float('inf')
        frequencies = defaultdict(int)
        required = len(cnt)
        while r < len(s):
            while r < len(s) and matches < required:
                if s[r] in cnt:
                    frequencies[s[r]] += 1
                    if frequencies[s[r]] == cnt[s[r]]:
                        matches += 1
                r += 1
            
            while l < r and matches == required:
                if r - l < res_len:
                    res_len = r - l
                    res_start = l

                if s[l] in cnt:
                    if frequencies[s[l]] == cnt[s[l]]:
                        matches -= 1
                    frequencies[s[l]] -= 1
                
                l += 1
        
        return '' if res_start == -1 else s[res_start:res_start + res_len]