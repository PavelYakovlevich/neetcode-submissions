class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                pairs += int(self.isPrefixAndSuffix(words[i], words[j]))
        return pairs
    
    def isPrefixAndSuffix(self, str1, str2) -> bool:
        if len(str1) > len(str2):
            return False
        
        L, R = 0, len(str2) - 1
        for i in range(len(str1)):
            if str2[L] != str1[i] or str2[R] != str1[-1 - i]:
                return False
            L += 1
            R -= 1
        
        return True