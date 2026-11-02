class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in seen:
            if num - 1 not in seen:
                offset = 0
                while num + offset in seen:
                    offset += 1
                longest = max(longest, offset)
        
        return longest