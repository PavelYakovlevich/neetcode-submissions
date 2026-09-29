class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq, rq = deque(), deque()
        n = len(senate)
        for i, s in enumerate(senate):
            if s == 'R':
                rq.append([s, i])
            else:
                dq.append([s, i])
        
        while dq and rq:
            if rq[0][-1] < dq[0][-1]:
                dq.popleft()
                senator, index = rq.popleft()
                rq.append([senator, index + n])
            else:
                rq.popleft()
                senator, index = dq.popleft()
                dq.append([senator, index + n])
        
        return 'Radiant' if rq else 'Dire'
