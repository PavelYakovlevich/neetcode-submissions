class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if n == 1:
            return 0
        
        meetings.sort(key=lambda meeting: meeting[0])

        unused_rooms = list(range(n))
        heapq.heapify(unused_rooms)
        used_rooms = []  # (end_time, room_number)
        
        meetings_counts = [0] * n

        for start, end in meetings:
            while used_rooms and used_rooms[0][0] <= start:
                _, r_number = heapq.heappop(used_rooms)
                heapq.heappush(unused_rooms, r_number)

            duration = end - start
            if unused_rooms:
                r_number = heapq.heappop(unused_rooms)
                heapq.heappush(used_rooms, (end, r_number))
            else:
                r_end_time, r_number = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, (r_end_time + duration, r_number))
            
            meetings_counts[r_number] += 1
        
        return meetings_counts.index(max(meetings_counts))