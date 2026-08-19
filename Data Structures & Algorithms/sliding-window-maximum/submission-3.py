class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, res = [], []
        window = defaultdict(int)
        l = 0

        for r in range(len(nums)):
            window[nums[r]] += 1
            heapq.heappush(heap, -nums[r])
            
            if (r - l + 1) == k:
                while not window[-heap[0]]:
                    heapq.heappop(heap)
                
                res.append(-heap[0])
                window[nums[l]] -= 1
                l += 1

        return res