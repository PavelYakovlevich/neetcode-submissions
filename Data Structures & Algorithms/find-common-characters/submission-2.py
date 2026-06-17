class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        for i in range(1, len(words)):
            counter = counter & Counter(words[i])

        res = []
        for ch, freq in counter.items():
            res.extend([ch] * freq)
        
        return res