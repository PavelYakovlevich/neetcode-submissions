import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        for start, end in sorted(intervals):
            if heap and heap[0] < start:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)