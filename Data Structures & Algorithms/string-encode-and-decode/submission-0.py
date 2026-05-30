class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += f"{len(s)}#{s}"

        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        
        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            
            word_length = int(s[i:j])

            i = j + 1
            j = i + word_length

            res.append(s[i:j])

            i = j
        
        return res