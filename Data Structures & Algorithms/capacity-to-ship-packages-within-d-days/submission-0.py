class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def can_ship(cap):
            ships = 1
            curr_cap = cap
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    curr_cap = cap
                curr_cap -= w

            return ships <= days

        while l <= r:
            capacity = (r + l) // 2
            if can_ship(capacity):
                res = min(res, capacity)
                r = capacity - 1
            else:
                l = capacity + 1

        return res