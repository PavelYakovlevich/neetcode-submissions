class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        res = 0
        
        for word in words:
            if allowed_set.issuperset(set(word)):
                res += 1

        return res
