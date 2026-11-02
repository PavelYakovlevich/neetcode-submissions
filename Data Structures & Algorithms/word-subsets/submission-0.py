from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_cnt2 = Counter()
        for w in words2:
            for char, count in Counter(w).items():
                max_cnt2[char] = max(max_cnt2[char], count)
        
        subsets = []    
        for w in words1:
            cnt1 = Counter(w)
            if not (max_cnt2 - cnt1):
                subsets.append(w)
        
        return subsets