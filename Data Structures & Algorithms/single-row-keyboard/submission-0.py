class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        positions = {char: i for i, char in enumerate(keyboard)}

        time = curr_pos = 0
        for printable_char in word:
            time += abs(curr_pos - positions[printable_char])
            curr_pos = positions[printable_char]
        
        return time
        