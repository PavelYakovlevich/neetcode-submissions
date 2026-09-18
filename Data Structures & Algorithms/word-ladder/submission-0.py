class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)

        transformations = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if self.can_transform(wordList[i], wordList[j]):
                    transformations[wordList[i]].append(wordList[j])
                    transformations[wordList[j]].append(wordList[i])
            
        q = deque([[beginWord, 1]])
        seen = set()

        while q:
            curr_word, transformation_count = q.popleft()

            if curr_word == endWord:
                return transformation_count

            for next_word in transformations[curr_word]:
                if next_word not in seen:
                    q.append([next_word, transformation_count + 1])
                    seen.add(next_word)

        return 0


    def can_transform(self, str1: str, str2: str) -> bool:
        unmatches_left = 1
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if not unmatches_left:
                    return False
                unmatches_left -= 1
        return True