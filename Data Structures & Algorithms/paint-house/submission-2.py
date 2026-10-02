class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cache = {}

        def dfs(house, prev_color):
            if (house, prev_color) in cache:
                return cache[(house, prev_color)]

            if house == len(costs):
                return 0
            
            min_cost = float('inf')
            for color in range(3):
                if color != prev_color:
                    min_cost = min(min_cost, costs[house][color] + dfs(house + 1, color))

            cache[(house, prev_color)] = min_cost

            return cache[(house, prev_color)]

        return dfs(0, -1)