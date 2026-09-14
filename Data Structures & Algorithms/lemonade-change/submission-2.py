class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = defaultdict(int)

        for bill in bills:
            cash[bill] += 1
            change = bill - 5

            if change > 5:
                if cash[10]:
                    change -= 10
                    cash[10] -= 1
                cash[5] -= change // 5
            elif change > 0:
                cash[5] -= 1
            
            if min(cash[5], cash[10]) < 0:
                return False

            
        return True