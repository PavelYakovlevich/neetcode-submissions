class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            elif stones[-1] < stones[-2]:
                stones[-2] -= stones[-1]
                stones.pop()
            else:
                stones[-1] -= stones[-2]
                stones.pop(len(stones) - 2)

        
        return stones[0] if len(stones) > 0 else 0