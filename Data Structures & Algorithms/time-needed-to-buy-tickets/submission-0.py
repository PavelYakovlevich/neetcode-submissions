class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        time = 0

        while True:
            if tickets[i] > 0:
                time += 1
                if i == k and tickets[i] == 1:
                    return time
                tickets[i] -= 1
                
            i = (i + 1) % len(tickets)