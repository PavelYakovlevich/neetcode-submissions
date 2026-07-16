class Solution:
    def normalize(self, email: str) -> str:
        res = []
        was_plus_met = False
        include_all = False
        for char in email:
            if include_all:
                res.append(char)
                continue

            if char == '@':
                include_all = True
                res.append(char)
            elif char == '.':
                continue
            elif char == '+':
                was_plus_met = True

            if not was_plus_met:
                res.append(char)
                
        return ''.join(res)

    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()

        for email in emails:
            normalized = self.normalize(email)
            res.add(normalized)
        
        return len(res)