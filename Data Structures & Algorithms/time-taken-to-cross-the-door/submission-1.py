class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        if not arrival:
            return []

        enter_q, exit_q = deque(), deque()

        answer = [0] * len(arrival)
        i, prev_use, time = 0, -1, arrival[0]
        while enter_q or exit_q or i < len(arrival):
            while i < len(arrival) and arrival[i] <= time:
                if state[i] == 0:
                    enter_q.append(i)
                else:
                    exit_q.append(i)
                i += 1
            
            target_q = None
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