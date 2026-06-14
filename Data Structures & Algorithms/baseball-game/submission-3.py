class Solution:
    def calPoints(self, operations: List[str]) -> int:
        operands = []
        for operation in operations:
            if operation == 'D':
                operands.append(operands[-1] * 2)
            elif operation == 'C':
                operands.pop()
            elif operation == '+':
                operands.append(operands[-1] + operands[-2])
            else:
                operands.append(int(operation))
        
        return sum(operands)