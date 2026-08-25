class FirstUnique:

    def __init__(self, nums: List[int]):
        self.__set = set()
        self.__q = deque()
        
        cnt = Counter(nums)
        for num in nums:
            if cnt[num] == 1:
                self.add(num)

    def showFirstUnique(self) -> int:
        return self.__q[0] if self.__q else -1

    def add(self, value: int) -> None:
        if value in self.__set:
            self.__q.remove(value)
            self.__set.remove(value)
            return
        
        self.__set.add(value)
        self.__q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
