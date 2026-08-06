class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        enriched_tasks_info = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)], reverse=True)
        
        heap = []        
        res = []    
        cpu_time = enriched_tasks_info[-1][0]  

        while len(res) < len(tasks):
            while enriched_tasks_info and enriched_tasks_info[-1][0] <= cpu_time:
                _, duration, index = enriched_tasks_info.pop()
                heapq.heappush(heap, (duration, index))

            if heap:
                processed_task_ex_time, index = heapq.heappop(heap)
                cpu_time += processed_task_ex_time
                res.append(index)
            elif enriched_tasks_info:
                cpu_time = enriched_tasks_info[-1][0]  

        return res