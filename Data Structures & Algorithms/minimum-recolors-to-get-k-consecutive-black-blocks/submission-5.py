class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L, R = 0, 0
        cnt = 0
        while R < k:
            cnt += 1 if blocks[R] == 'W' else 0
            R += 1 
        res = cnt

        while R < len(blocks):
            cnt += 1 if blocks[R] == 'W' else 0
            cnt -= 1 if blocks[L] == 'W' else 0

            R += 1
            L += 1

            res = min(cnt, res)
        return res