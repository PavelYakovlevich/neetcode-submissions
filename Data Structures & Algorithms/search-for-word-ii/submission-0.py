class TrieNode:
    def __init__(self, is_word=False):
        self.children = {}
        self.is_word = is_word

class Trie:
    def __init__(self, words: List[str]):
        self.__root = TrieNode()
        for word in words:
            self.add_word(word)
    
    def add_word(self, word: str):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True
    
    def search(self, word: List[str]):
        curr = self.__root
        for char in word:
            if char not in curr.children:
                return (False, False)
            curr = curr.children[char]
        return (True, curr.is_word)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)
        ROWS, COLS = len(board), len(board[0])
        res = set()
        curr_word = []
        visited = set()
        def search_words(r, c):
            visited.add((r, c))
            curr_word.append(board[r][c])

            contains_curr_word, is_word_found = trie.search(curr_word)
            if not contains_curr_word:
                curr_word.pop()
                visited.remove((r, c))
                return False
            
            if is_word_found:
                res.add(''.join(curr_word))
            
            for r_adj, c_adj in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
                new_r, new_c = r + r_adj, c + c_adj
                if (min(new_r, new_c) >= 0 and
                    new_r < ROWS and
                    new_c < COLS and
                    (new_r, new_c) not in visited):
                    search_words(new_r, new_c)

            curr_word.pop()
            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                search_words(r, c)

        return list(res)