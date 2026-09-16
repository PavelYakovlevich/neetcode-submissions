class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotation_map = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6
        }

        rotated_n, num = 0, n
        while num:
            if num % 10 in rotation_map:
                rotated_n = rotated_n * 10 + rotation_map[num % 10]
                num //= 10
            else:
                return False
        
        return rotated_n != n