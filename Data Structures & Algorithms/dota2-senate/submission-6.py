class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        cnt = Counter(senate)
        q = deque(senate)
        banned_dire = banned_radiant = 0
        while cnt['R'] and cnt['D']:
            while (q[0] == 'R' and banned_radiant) or (q[0] == 'D' and banned_dire):
                senator = q.popleft()
                if senator == 'R':
                    banned_radiant -= 1
                    cnt['R'] -= 1
                else:
                    banned_dire -= 1
                    cnt['D'] -= 1

            senator = q.popleft()                
            if senator == 'R':
                banned_dire += 1
            else:
                banned_radiant += 1
            q.append(senator)

        return 'Radiant' if q[0] == 'R' else 'Dire'