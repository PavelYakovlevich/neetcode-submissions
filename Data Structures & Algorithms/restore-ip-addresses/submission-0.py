class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtracking(i, dots, ip): 
            if i == len(s):
                if dots == 4:
                    res.append(ip[:-1])
                return
            if dots > 4:
                return
            
            for j in range(i, min(i + 3, len(s))):
                if i != j and s[i] == "0":
                    continue
                if int(s[i: j + 1]) < 256:
                    backtracking(j + 1, dots + 1, ip + s[i: j + 1] + ".")

        backtracking(0, 0, '')
        return res


