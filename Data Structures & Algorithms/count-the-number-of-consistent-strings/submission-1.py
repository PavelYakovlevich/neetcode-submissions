class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        res = 0
        
        for word in words:
            if set(word).issubset(allowed_set):
                res += 1

        return res
