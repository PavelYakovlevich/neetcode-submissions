class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [[num, i] for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for i in range(k):
            num, index = heapq.heappop(heap)
            nums[index] *= multiplier
            heapq.heappush(heap, [nums[index], index])
        
        return nums