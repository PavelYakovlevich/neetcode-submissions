class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = -1
        i = 0
        while i + k - 1 < len(blocks):
            cnt = 0
            for j in range(i, i + k):
                cnt += 1 if blocks[j] == 'W' else 0
            
            res = cnt if res == -1 else min(res, cnt)
            i += 1
        
        return res