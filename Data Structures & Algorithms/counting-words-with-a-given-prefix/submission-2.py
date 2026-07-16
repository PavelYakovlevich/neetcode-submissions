class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        cnt = 0

        for word in words:
            cnt += int(word.startswith(pref))
        
        return cnt