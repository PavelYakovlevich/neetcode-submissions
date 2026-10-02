"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
            
        intvs = []
        for intv in intervals:
            intvs.append([intv.start, intv.end])
        intvs.sort(key=lambda x: x[0])
        
        heap = [intvs[0][-1]]
        for i in range(1, len(intvs)):
            start, end = intvs[i]
            if start >= heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, end)

        return len(heap)
