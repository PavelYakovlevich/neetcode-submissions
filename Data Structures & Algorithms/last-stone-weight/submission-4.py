class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            diff = abs(heapq.heappop_max(stones) - heapq.heappop_max(stones))
            if diff:
                heapq.heappush_max(stones, diff)

        return stones[0] if len(stones) else 0