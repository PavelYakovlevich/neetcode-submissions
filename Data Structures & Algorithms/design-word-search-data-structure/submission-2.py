class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.__root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.__root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            
            curr = curr.children[char]
        
        curr.word = True

    def search(self, word: str) -> bool:
        return self.__search_core(self.__root, word, 0)

    def __search_core(self, node: TrieNode, word: str, index: int) -> bool:
        curr = node

        for i in range(index, len(word)):
            char = word[i]

            if char == '.':
                for child in curr.children.values():
                    if self.__search_core(child, word, i + 1):
                        return True
                return False
            
            if char not in curr.children:
                return False
            
            curr = curr.children[char]
        
        return curr.word
