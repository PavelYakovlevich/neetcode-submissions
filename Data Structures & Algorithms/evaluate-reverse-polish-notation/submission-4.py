class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a, b: b + a,
            '-': lambda a, b: b - a,
            '*': lambda a, b: b * a,
            '/': lambda a, b: int(b / a)
        }

        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(int(token))
            else:
                res = operations[token](stack.pop(), stack.pop())
                stack.append(res)
        
        return stack[0]