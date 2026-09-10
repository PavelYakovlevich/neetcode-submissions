class StringIterator:

    def __init__(self, compressedString: str):
        self.__str = compressedString
        self.__curr = ['', 0, 0]

    def next(self) -> str:
        if not self.hasNext():
            return ' '
        
        char, count, index = self.__curr
        if index < 0 or not count:
            char = self.__str[index]
            index += 1
            
            while index < len(self.__str) and self.__str[index].isdigit():
                count = count * 10 + int(self.__str[index])
                index += 1
            
            self.__curr = [char, count, index]


        self.__curr[1] -= 1
        return self.__curr[0]

    def hasNext(self) -> bool:
        return self.__curr[-1] < len(self.__str) or self.__curr[1] > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
