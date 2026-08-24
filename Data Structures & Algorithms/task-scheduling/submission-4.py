class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        cnt = Counter(tasks)

        heap = []
        for task, count in cnt.items():
            heapq.heappush(heap, (-count))
            
        waiting_q = deque()
        tick = 0
        while heap or waiting_q:
            while waiting_q and waiting_q[0][0] <= tick:
                time, count = waiting_q.popleft()
                heapq.heappush(heap, -count)
            
            if heap:
                count = -heapq.heappop(heap)
                if count > 1:
                    waiting_q.append((tick + n + 1, count - 1))
                
            tick += 1
        
        return tick