class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26

        for char in magazine:
            cnt[ord(char) - ord('a')] += 1
        for char in ransomNote:
            if not cnt[ord(char) - ord('a')]:
                return False
            cnt[ord(char) - ord('a')] -= 1
        
        return True
