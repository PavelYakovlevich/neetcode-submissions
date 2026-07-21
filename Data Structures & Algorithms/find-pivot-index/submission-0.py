class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sums = []
        total = 0

        for num in nums:
            total += num
            prefix_sums.append(total)
        
        for i in range(len(prefix_sums)):
            left = prefix_sums[i - 1] if i > 0 else 0
            right = prefix_sums[-1] - prefix_sums[i]

            if left == right:
                return i

        return -1