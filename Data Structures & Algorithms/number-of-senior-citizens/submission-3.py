class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors_count = 0

        for detail in details:
            age = 10 * int(detail[-4]) + int(detail[-3])
            seniors_count += int(age > 60)

        return seniors_count