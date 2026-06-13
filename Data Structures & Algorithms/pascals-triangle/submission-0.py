class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(numRows):
            res.append([])
            for k in range(n + 1):
                res[n].append(math.factorial(n) // (math.factorial(k) * math.factorial(n - k)))
        return res