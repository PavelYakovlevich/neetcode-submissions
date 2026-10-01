class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq = defaultdict(int)
        for char in text:
            if char in ['l', 'o']:
                freq[char] += 0.5
            else:
                freq[char] += 1
        
        res = freq['b']
        for char in ['b', 'l', 'a', 'o', 'n']:
            res = min(res, int(freq[char]))
        
        return res
