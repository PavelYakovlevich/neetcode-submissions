class Solution:
    def tribonacci(self, n: int) -> int:
        if not n: 
            return 0
        
        sums = [0, 1, 1]
        for i in range(3, n + 1):
            next_num = sum(sums)
            sums[0], sums[1] = sums[1], sums[2]
            sums[2] = next_num
        
        return sums[-1]
