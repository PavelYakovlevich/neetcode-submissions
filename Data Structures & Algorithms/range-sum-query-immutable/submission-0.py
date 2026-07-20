class NumArray:

    def __init__(self, nums: List[int]):
        self.__prefixes = []
        acc =- 0
        
        for num in nums:
            acc += num
            self.__prefixes.append(acc)


    def sumRange(self, left: int, right: int) -> int:
        right_pos = self.__prefixes[right]
        left_pos = self.__prefixes[left - 1] if left > 0 else 0

        return right_pos - left_pos


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)