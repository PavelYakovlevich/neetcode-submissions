class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            int_sum = numbers[l] + numbers[r]
            if int_sum > target:
                r -= 1
            elif int_sum < target:
                l += 1
            else:
                return [l + 1, r + 1]