class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        similarities = set()
        for u, v in similarPairs:
            similarities.add((u, v))
            similarities.add((v, u))

        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and (sentence1[i], sentence2[i]) not in similarities:
                return False
        
        return True