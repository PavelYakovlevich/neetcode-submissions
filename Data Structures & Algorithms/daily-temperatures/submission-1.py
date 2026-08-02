class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                prev_temp, prev_temp_index = stack.pop()
                res[prev_temp_index] = i - prev_temp_index
            stack.append((t, i))

        return res