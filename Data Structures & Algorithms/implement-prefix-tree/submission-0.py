class Node:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.__root = Node()

    def insert(self, word: str) -> None:
        curr = self.__root

        for char in word:
            if char not in curr.children:
                curr.children[char] = Node()
            curr = curr.children[char]

        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.__root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.__root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True