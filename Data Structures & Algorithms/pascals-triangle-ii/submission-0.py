class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1] if not rowIndex else [1, 1]
        
        row = [1, 1]
        for r_index in range(2, rowIndex + 1):
            next_row = [1]
            for i in range(1, len(row)):
                next_row.append(row[i] + row[i - 1])
            next_row.append(1)
            row = next_row
        
        return row