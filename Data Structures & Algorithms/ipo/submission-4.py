class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = [(capital[i], profits[i]) for i in range(len(capital))]

        projects.sort()

        candidates_projects = []
        
        ptr = 0
        while k > 0:
            while ptr < len(projects) and projects[ptr][0] <= w:
                heapq.heappush(candidates_projects, -projects[ptr][1])
                ptr += 1

            if candidates_projects:
                chosen_profit = -heapq.heappop(candidates_projects)
                w += chosen_profit
            else:
                break

            k -= 1

        return w