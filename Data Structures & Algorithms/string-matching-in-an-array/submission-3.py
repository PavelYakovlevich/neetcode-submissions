class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                
                if words[j] in words[i] and words[j] not in res:
                    res.add(words[j])

        return list(res)