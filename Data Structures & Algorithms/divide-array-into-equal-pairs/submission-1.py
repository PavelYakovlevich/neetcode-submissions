class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = Counter(nums)

        for num, count in cnt.items():
            if count % 2 != 0:
                return False
        
        return True