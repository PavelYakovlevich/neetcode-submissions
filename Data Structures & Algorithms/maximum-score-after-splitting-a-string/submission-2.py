class Solution:
    def maxScore(self, s: str) -> int:
        right_score = s.count('1')
        max_score = 0
        left_score = 0
        for i in range(0, len(s) - 1):
            left_score += int(s[i] == '0')
            right_score -= int(s[i] == '1')
            max_score = max(max_score, left_score + right_score)

        return max_score
        
