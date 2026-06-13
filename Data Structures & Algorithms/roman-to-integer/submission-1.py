class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = num_map[s[0]]
        for i in range(1, len(s)):
            res += num_map[s[i]]
            if s[i] in ['V', 'X'] and s[i - 1] == 'I':
                res -= 2 * num_map['I']
            elif s[i] in ['L', 'C'] and s[i - 1] == 'X':
                res -= 2 * num_map['X']
            elif s[i] in ['D', 'M'] and s[i - 1] == 'C':
                res -= 2 * num_map['C']

        return res

                

        