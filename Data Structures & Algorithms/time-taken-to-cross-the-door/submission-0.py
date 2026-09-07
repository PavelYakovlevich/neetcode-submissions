class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        if not arrival:
            return []

        enter_q, exit_q = deque(), deque()

        def add_to_queue(index: int):
            if state[index] == 0:
                enter_q.append(index)
            else:
                exit_q.append(index)

        add_to_queue(0)

        answer = [0] * len(arrival)
        i, prev_use, time = 1, -1, arrival[0]
        target_q = None
        while enter_q or exit_q or i < len(arrival):
            while i < len(arrival) and arrival[i] <= time:
                add_to_queue(i)
                i += 1
            
            if exit_q and enter_q:
                target_q = enter_q if prev_use == 0 else exit_q
            else:
                target_q = exit_q or enter_q

            if target_q:
                person_idx = target_q.popleft()
                answer[person_idx] = time
                prev_use = state[person_idx]
                time += 1
            else:
                prev_use = -1
                time = arrival[i] if i < len(arrival) else time + 1

        return answer