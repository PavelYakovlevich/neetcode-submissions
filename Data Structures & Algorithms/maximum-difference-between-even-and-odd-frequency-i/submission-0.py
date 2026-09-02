class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = Counter(s)
        
        max_odd, min_even = 0, float('inf')
        for _, count in cnt.items():
            if count % 2 != 0:
                max_odd = max(max_odd, count)
            else:
                min_even = min(min_even, count)
        
        return max_odd - min_even