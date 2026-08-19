class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        cnt = Counter(s1)
        window = Counter()
        l = 0
        for r in range(0, len(s2)):
            window[s2[r]] += 1

            if (r - l + 1) < len(s1):
                continue

            if window == cnt:
                return True
            
            window[s2[l]] -= 1
            l += 1

        return False