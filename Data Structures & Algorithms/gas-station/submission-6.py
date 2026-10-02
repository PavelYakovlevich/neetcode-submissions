class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        n = len(gas)
        res = curr_gas = 0
        for i in range(n):
            if curr_gas < 0:
                curr_gas = 0
                res = i
            curr_gas += gas[i] - cost[i]
        return res