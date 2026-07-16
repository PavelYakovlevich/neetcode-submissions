class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while True:
            diff = numbers[L] + numbers[R]

            if diff == target:
                return [L + 1, R + 1]
            elif diff < target:
                L += 1
            else:
                R -= 1