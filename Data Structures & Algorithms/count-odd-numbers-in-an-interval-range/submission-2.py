class Solution:
    def countOdds(self, low: int, high: int) -> int:
        seq_len = high - low + 1
        if seq_len & 1:
            if low & 1:
                return int(seq_len / 2) + 1
            return int(seq_len / 2)
        
        return seq_len // 2