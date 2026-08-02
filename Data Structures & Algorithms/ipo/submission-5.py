class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        min_heap = [(c, p) for c, p in zip(capital, profits)]
        max_heap = []

        heapq.heapify(min_heap)

        for i in range(k):
            while min_heap and min_heap[0][0] <= w:
                _, p = heapq.heappop(min_heap)
                heapq.heappush_max(max_heap, p)
            
            if max_heap:
                w += heapq.heappop_max(max_heap)
            else:
                break
        
        return w
