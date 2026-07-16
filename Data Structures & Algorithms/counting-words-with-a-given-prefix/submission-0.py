class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0

        for word in words:
            i = 0
            while i < min(len(pref), len(word)):
                if pref[i] != word[i]:
                    break
                i += 1

            cnt += 1 if i == len(pref) else 0
        
        return cnt