class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(reverse=True)
        queries_info = sorted([(q, i) for i, q in enumerate(queries)])

        # (length, end)
        intv_heap = []
        res = [-1] * len(queries)
        for q, pos in queries_info:
            while intervals and intervals[-1][0] <= q:
                interval = intervals.pop()
                heapq.heappush(intv_heap, (interval[1] - interval[0] + 1, interval[1]))

            while intv_heap and intv_heap[0][1] < q:
                heapq.heappop(intv_heap)
            
            if intv_heap:
                res[pos] = intv_heap[0][0]
        
        return res