class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = [False] * 26

        for ch in allowed:
            allowed_set[ord(ch) - ord('a')] = True
        
        res = len(words)
        for word in words:
            for ch in word:
                if not allowed_set[ord(ch) - ord('a')]:
                    res -= 1
                    break

        return res