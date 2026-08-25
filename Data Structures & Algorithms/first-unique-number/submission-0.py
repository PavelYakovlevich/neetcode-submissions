class FirstUnique:

    def __init__(self, nums: List[int]):
        self.__cnt = Counter(nums)
        self.__q = deque()
        for num in nums:
            if self.__cnt[num] < 2:
                self.__q.append(num)

    def showFirstUnique(self) -> int:
        while self.__q:
            count = self.__cnt[self.__q[0]]
            if count == 1:
                return self.__q[0]
            self.__q.popleft()
        
        return -1

    def add(self, value: int) -> None:
        self.__cnt[value] += 1
        self.__q.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
