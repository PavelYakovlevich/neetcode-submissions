class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        for i in range(1, len(words)):
            counter = counter & Counter(words[i])

        res = []
        for item in counter.items():
            for i in range(item[1]):
                res.append(item[0])
        
        return res