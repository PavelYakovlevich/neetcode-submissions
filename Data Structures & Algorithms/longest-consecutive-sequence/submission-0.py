class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest_seq_len = 0

        for num in nums:
            if (num - 1) not in nums_set:
                seq_len = 0

                while (num + seq_len) in nums_set:
                    seq_len += 1
                
                longest_seq_len = max(longest_seq_len, seq_len)
        
        return longest_seq_len