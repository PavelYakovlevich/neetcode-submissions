class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        greed_idx = size_idx = 0
    
        while greed_idx < len(g) and size_idx < len(s):
            if g[greed_idx] <= s[size_idx]:
                greed_idx += 1

            size_idx += 1
        
        return greed_idx

