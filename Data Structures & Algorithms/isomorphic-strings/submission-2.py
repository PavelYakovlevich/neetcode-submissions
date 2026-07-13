class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map = {}
        seen = set()
        for i in range(len(s)):
            if s[i] not in map:
                if t[i] in seen:
                    return False
                    
                map[s[i]] = t[i]
                seen.add(t[i])
                continue
            
            if t[i] != map[s[i]]:
                return False
            

        
        return True