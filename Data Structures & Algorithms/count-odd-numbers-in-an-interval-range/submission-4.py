class Solution:
    def countOdds(self, low: int, high: int) -> int:
        seq_len = high - low + 1
        if seq_len & 1:
            return seq_len // 2 + (low & 1)
        
        return seq_len // 2